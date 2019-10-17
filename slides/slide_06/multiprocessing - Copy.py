from apiscout.ApiScout import ApiScout
from multiprocessing import Pool, cpu_count

apiscout = ApiScout()
apiscout.setBaseAddress(0)
apiscout.loadWinApi1024('data/winapi1024v1.txt')
vector_a = "A22gA5BA35QA17gACA3Q ... fpT}/Mp-.n?"
vector_b = "A64IA13CA5RA13wAABA5 ... ACIECmth.n?"

range_vals =  [x for x in (i*10**exp for exp in range(0, 6) for i in range(1, 11))]

def parallel_apiscout(Q):
    (vector_a, vector_b) = Q
    return apiscout.matchVectors(vector_a, vector_b)

for numbers in range_vals:
    list_b = [vector_b] * numbers 

    with Pool(cpu_count()) as p:
        p.map(parallel_apiscout, [(vector_a, x) for x in list_b])