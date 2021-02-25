
n = 1000000
m = 7
l = 7

a = []
for i in range(l * (10 ** 2), n):
    if i % m == 0 and str(i)[-3] == str(l):
        a.append(i)
    else:
        continue

Answer = sum(a)
print(Answer)