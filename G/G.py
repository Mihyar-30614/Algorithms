import sys

Lines = list()
count = 0

def check(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return 0
    return 1

T = int(sys.stdin.readline())
for i in range(T):
    line = sys.stdin.readline().split()
    X1 = float(line[0])
    Y1 = float(line[1])
    X2 = float(line[2])
    Y2 = float(line[3])
    Lines.append([[X1,Y1],[X2,Y2]])

for i in range(0,T):
    first = Lines[i]
    for j in range(i+1,T):
        second = Lines[j]
        count += check(first,second)

print(count)