from apiscout.ApiScout import ApiScout

apiscout = ApiScout()
apiscout.setBaseAddress(0)
apiscout.loadWinApi1024('data/winapi1024v1.txt')
vector_a = "A22gA5BA35QA17gACA3Q ... fpT}/Mp-.n?"
vector_b = "A64IA13CA5RA13wAABA5 ... ACIECmth.n?"

range_vals =  1000000

for number in range(range_vals):
    apiscout.matchVectors(vector_a, vector_b)