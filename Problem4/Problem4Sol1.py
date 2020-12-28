import time

Ti = time.time()

Nmin = 100
SS = 1655
Nmax = 1000000
a = []
for i in range(Nmin, Nmax):
    DivisorCount = 0
    b = int(i ** 0.5)
    Divisor = set([])
    for j in range(1, b + 1):
        if i % j == 0 and j * (i // j) == i:
            Divisor.add(j)
            Divisor.add(i/j)
        else:
            pass
        if len(Divisor) <= 4:
            continue
        else:
            break
    if len(Divisor) == 4:
        a.append(i)
    else:
        continue


Answer = sum(a) + SS
print(Answer)
Tf = time.time()
print("time: %s s" % (Tf-Ti))
