import time

Ti = time.time()

Nmin = 1
Nmax = 1000000
DivisorCount = 4

Det = [2] * Nmax
Det[0] = 0
Det[1] = 1

for i in range(2, int(Nmax / 2) + 1):
    a = 2 * i
    while a < Nmax:
        Det[a] = Det[a] + 1
        a = a + i

Result = [k for k, ele in enumerate(Det) if ele == DivisorCount]
Answer = sum(Result)
print(Answer)
Tf = time.time()
print("time: %s s" % (Tf-Ti))