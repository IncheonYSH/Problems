
n = 100000
m = 6

def pi(N):
    Nstr = str(N)
    a = 1
    for i in range(0, len(Nstr)):
        a = a * int(Nstr[i])
    return a

def f(N):
    b = pi(N)
    while len(str(b)) > 1:
        b = pi(b)
    return(b)

nn = []
for i in range(1, n):
    if f(i) == m:
        nn.append(i)
    else:
        continue

Answer = sum(nn)
print(Answer)

