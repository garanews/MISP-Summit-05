import cupy as cp

ruzicka_shared_kernel = cp.RawKernel(r"""
    extern "C" __global__
    #define TILE_WIDTH 32
    void shared_ruzicka(const unsigned short* x1, const unsigned short* x2, 
                        float* y, int width, int height) {
        __shared__ unsigned short x1s[TILE_WIDTH][TILE_WIDTH];
        __shared__ unsigned short x2s[TILE_WIDTH];
        int by = blockIdx.y; int tx = threadIdx.x; int ty = threadIdx.y;
        int row = by * TILE_WIDTH + ty;
        int idx = 0;
        unsigned short tmp = 0;
        float maxab = minab = 0.0;

        for (int m = 0; m < 1024/TILE_WIDTH; ++m){
            idx = row * width + m * TILE_WIDTH + tx;
            if (idx < width * height){
                x1s[ty][tx] = x1[idx];
                x2s[tx] = x2[m*TILE_WIDTH + tx];
                __syncthreads();
                for (int k=0; k < TILE_WIDTH; ++k){
                    tmp = x1s[ty][k] * (1023 - (m*TILE_WIDTH+k));
                    if(x2s[k] > tmp){ maxab += x2s[k]; minab += tmp; }
                    else{ minab += x2s[k]; maxab += tmp; }
                }
                __syncthreads();
            }}
        y[row] = minab / maxab;
    }""", "shared_ruzicka",
)

def ruzicka_shared_retval(a, b):
    y = cp.zeros(CHUNKSIZE, dtype=cp.float32).reshape(1, CHUNKSIZE)
    ruzicka_shared_kernel((32, (len(a) + 31) // 32), (32, 32), (a, b, y, 1024, len(a)))
    return y

dda = da.from_zarr('malware_database.zarr', chunks=(100000,1024))
res = dda.map_blocks(lambda df: ruzicka_shared_retval(cp.array(df), vector_new), 
                     dtype=cp.float32).compute()