import sys
from fractions import gcd
from functools import reduce

# Read the Number of lines
line = sys.stdin.readline().split()
N = int(line[0])

# Define variables and initialize it
OH = [None for i in range(N)]
OW = [None for i in range(N)]
H = list()
W = list()
Stack = list()
max_area = 0

def find_gcd(list):
    x = reduce(gcd, list)
    return int(x)


for i in range(0, N):
	# Read the input
	line = sys.stdin.readline().split()
	OH[i] = int(line[0])
	OW[i] = int(line[1])
	
min_width = find_gcd(OW)

for i in range(0,N):
	temp = int(OW[i] / min_width)
	if OW[i] == min_width:
		H.append(OH[i])
		W.append(OW[i])
	else:
		for x in range(0,temp):
			H.append(OH[i])
			W.append(min_width)

N = len(H)	
i = 0
# Compute Area
while i < N:
	if (not Stack) or (H[Stack[-1]] <= H[i]):
		Stack.append(i)
		i += 1
	else:
		j = Stack.pop()
		area = ((H[j]* W[j]) * ((i - Stack[-1] -1) if Stack else i))
		max_area = max(max_area, area)

while Stack:
	j = Stack.pop()
	area = ((H[j]* W[j]) * ((i - Stack[-1] -1) if Stack else i))
	max_area = max(max_area, area)

print(max_area * 50)