Nmr1 = 47
Dnm1 = 245
Nmr2 = 34
Dnm2 = 177

a = 2
while True:
    n1 = Nmr1 * (a / Dnm1)
    n2 = Nmr2 * (a / Dnm2)
    if int(n2) - int(n1) == 0 or int(n2) == n2:
        a = a + 1
    else:
        n = int(n1) + 1
        m = a
        break

print("n : %d" % n, "m : %d" % m, "n + m : %d" % (m + n), sep = '\n')