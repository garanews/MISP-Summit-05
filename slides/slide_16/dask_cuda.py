import zarr
import dask
import dask.array as da
import dask.dataframe as dd
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
import cupy as cp

CHUNKSIZE = 100000

def ruzicka_cupy(vector_old, vector_new):
    vector_old_cp = cp.array(vector_old) * cp.arange(1023, -1, -1, dtype=cp.uint16)
    min_up = cp.minimum(vector_old_cp, vector_new)
    max_down = cp.maximum(vector_old_cp, vector_new)
    numerator = cp.sum(min_up, axis=1)
    denominator = cp.sum(max_down, axis=1)
    return cp.asnumpy(cp.divide(numerator, denominator))

if __name__ == "__main__":
    cluster = LocalCUDACluster(n_workers=8, threads_per_worker=8)
    client = Client(cluster)

    # GENERATE ONE RANDOM SAMPLE TO IDENTIFY
    vector_new = cp.array(cp.random.choice([0, 1], 1024), dtype=cp.uint16) * cp.arange(
        1023, -1, -1, dtype=cp.uint16
    )

    # DATABASE TO COMPARE
    d_da = da.from_zarr('malware_database.zarr', chunks=(CHUNKSIZE,1024))    
    d_dd = dd.from_dask_array(d_da)
    res = d_dd.map_partitions(
        lambda df: ruzicka_cupy(cp.array(df), vector_new),
            meta=("result", cp.float32),
    ).compute()
    client.close()