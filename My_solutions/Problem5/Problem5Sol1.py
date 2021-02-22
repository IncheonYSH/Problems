import sys
import time

Ti = time.time()
sys.stdin = open("input.txt", "r")

RadCount = int(sys.stdin.readline().split()[0])
Rad = [list(map(int, sys.stdin.readline().split())) for r in range(RadCount)]
BeamCount = int(sys.stdin.readline().split()[0])
Las = [list(map(int, sys.stdin.readline().split())) for l in range(BeamCount)]
LasS = [c[1] / c[0] for c in Las]
LasSlope = sorted(LasS)

Count = RadCount
for i in range(RadCount):
    Smin = Rad[i][1] / Rad[i][0]
    Smax = Rad[i][3] / Rad[i][2]
    if Smin > Smax:
        Smin, Smax = Smax, Smin
    else:
        pass
    if LasSlope[0] > Smax:
        continue
    elif LasSlope[-1] < Smin:
        continue
    else:
        '''
        Binary Search
        '''
        Left = 0
        Right = BeamCount - 1
        Mid = int((Left + Right) / 2)
        while True:
            if Left == Right == Mid:
                if Smin <= LasSlope[Mid] <= Smax:
                    Count = Count - 1
                else:
                    break
                break
            elif Smin <= LasSlope[Mid] <= Smax:
                Count = Count - 1
                break
            elif LasSlope[Mid] < Smin:
                Left = Mid + 1
                Mid = int((Left + Right) / 2)
            elif LasSlope[Mid] > Smax:
                Right = Mid - 1
                Mid = int((Left + Right) / 2)
            else:
                break

print(Count)
Tf = time.time()
print(Tf - Ti)
