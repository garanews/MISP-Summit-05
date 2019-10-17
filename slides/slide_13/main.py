# MAIN.PY
import zarr
import numpy as np
import dask.array as da

def ruzicka_func(vector_old, vector_new):
    from ruzi_cython import ruzicka
    return ruzicka.ruzicka(vector_new, vector_old)

if __name__ == "__main__":
    vector_new = np.array(np.random.choice(a=[0, 1], size=(1, 1024)), dtype=np.uint16)
    vector_weighted = vector_new[0] * np.arange(1023, -1, -1, dtype=np.uint16)
    df = da.from_zarr('/tmp/zarr100M_uint16_test.zarr', chunks=(100000, 1024))
    res = da.apply_along_axis(lambda x: ruzicka_func(x, vector_weighted), 1, df).compute()
