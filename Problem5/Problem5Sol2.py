import sys
import time

Ti = time.time()
sys.stdin = open("input.txt", "r")

RadCount = int(sys.stdin.readline().split()[0])
Rad = [sys.stdin.readline().split() for i in range(RadCount)]
BeamCount = int(sys.stdin.readline().split()[0])
Las = [sys.stdin.readline().split() for k in range(BeamCount)]

for j in range(RadCount):
    n = 0
    while n < BeamCount:
        x1 = int(Las[n][0])
        y1 = int(Las[n][1])
        if (x1 * int(Rad[j][1]) - y1 * int(Rad[j][0])) * (x1 * int(Rad[j][3]) - y1 * int(Rad[j][2])) <= 0:
            RadCount = RadCount - 1
            break
        else:
            n = n + 1

print(RadCount)
Tf = time.time()
print(Tf - Ti)

