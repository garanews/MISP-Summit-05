# RUZICKA.PY
import numpy as np
cimport numpy as np
cimport cython
# IMPORTING EXTERNAL C CODE FROM C_RUZICKA
ctypedef np.uint16_t data_type_16
cdef extern double c_ruzicka (data_type_16* array_a, data_type_16* array_b)
@cython.boundscheck(False)
@cython.wraparound(False)
def ruzicka(np.ndarray[data_type_16, ndim=1, mode="c"] vector_a, np.ndarray[data_type_16, ndim=1, mode="c"] vector_b):
    res = c_ruzicka(&vector_a[0], &vector_b[0])
    return res