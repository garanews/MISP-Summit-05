from apiscout.ApiScout import ApiScout
from multiprocessing import Pool, cpu_count

apiscout = ApiScout()
apiscout.setBaseAddress(0)
apiscout.loadWinApi1024('data/winapi1024v1.txt')
vector_a = "A22gA5BA35QA17gACA3Q ... fpT}/Mp-.n?"
vector_b = "A64IA13CA5RA13wAABA5 ... ACIECmth.n?"

range_vals =  1000000

def parallel_apiscout(Q):
    (vector_a, vector_b) = Q
    return apiscout.matchVectors(vector_a, vector_b)

with Pool(cpu_count()) as p:
    p.map(parallel_apiscout, [(vector_a, vector_b) for x in range(range_vals)])