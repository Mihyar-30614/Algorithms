import sys

# Read the input
line = sys.stdin.readline().split()
N = int(line[0])
M = int(line[1])
P = []

# Define Rows and Cols
row = int(N) + 2
col = int(M) + 2

# Define Arrays
H = [[0 for i in range(col)] for j in range(row)]
W = [[-1 for i in range(col)] for j in range(row)]

# Initialize WATER array
for i in range(0,row):
    line = W[i]
    if i == 0 or i == N+1:
        line = [0 for j in range(col)]
    else:
        line[0] = 0
        line[M+1] = 0
    W[i] = line

# Initialize HEIGHT array
for i in range(0,row):
    line = H[i]
    if i == 0 or i == N+1:
        line = [-1 for j in range(col)]
    else:
        line[0] = -1
        line[M+1] = -1
    H[i] = line

# Fill Water Array
def fillArray(x, y, h):
    W[x][y] = h
    if H[x-1][y] <= h and W[x-1][y] == -1:
        fillArray(x-1, y, h)
    if H[x][y-1] <= h and W[x][y-1] == -1:
        fillArray(x, y-1, h)
    if H[x+1][y] <= h and W[x+1][y] == -1:
        fillArray(x+1, y, h)
    if H[x][y+1] <= h and W[x][y+1] == -1:
        fillArray(x, y+1, h)

for i in range(1, N+1):
    line = sys.stdin.readline().split()
    intline = [int(num) for num in line]
    H[i][1:N+1] = intline

for i in range(1, N+1):
    for j in range(1, M+1):
        P.append([H[i][j], i, j])

P.sort()
for pair in P:
    x = pair[1]
    y = pair[2]
    h = pair[0]

    if W[x-1][y] != -1 or W[x][y-1] != -1 or W[x+1][y] != -1 or W[x][y+1] != -1:
        fillArray(x, y, h)

for i in range(1, N+1):
    line = ''
    for j in range(1, M+1):
        temp = W[i][j] - H[i][j]
        line += str(temp) + ' '
    print(line.strip())
