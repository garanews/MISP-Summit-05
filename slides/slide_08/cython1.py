import numpy as np
cimport numpy as np
from multiprocessing import Pool, cpu_count

# n_decompress & _n_apply_weights are the same function used by apivector

cdef double ruzicka(x, y):
    cdef int[:] ix, iy, vector_a, vector_b 
    if len(x) != 1024:
        ix = n_decompress(x)
    vector_a = _n_apply_weights(ix)
    if len(y) != 1024:
        iy = n_decompress(y)
    vector_b = _n_apply_weights(iy)
    cdef double maxPQ = np.sum(np.maximum(vector_a, vector_b))
    return np.sum(np.minimum(vector_a, vector_b))/maxPQ

def run_cython(Q):
    (vector_a, vector_b) = Q
    return ruzicka(vector_a, vector_b)

with Pool(cpu_count()) as p:
    p.map(run_cython, [(vector_a, vector_b) for x in range(range_vals)])