import numpy as np
import cupy as cp

def ruzicka_numpy(vector_old, vector_new):
    vector_old =  vector_old * np.arange(1023, -1, -1, dtype=np.uint16)
    min_up = np.minimum(vector_old, vector_new)
    max_down = np.maximum(vector_old, vector_new)
    numerator = np.sum(min_up)
    denominator = np.sum(max_down)
    return np.divide(numerator, denominator)

def ruzicka_cupy(vector_old, vector_new):
    vector_old = vector_old * cp.arange(1023, -1, -1, dtype=cp.uint16)
    min_up = cp.minimum(cp.array(vector_old), vector_new)
    max_down = cp.maximum(cp.array(vector_old), vector_new)
    numerator = cp.sum(min_up, axis=1)
    denominator = cp.sum(max_down, axis=1)
    return cp.asnumpy(cp.divide(numerator, denominator))