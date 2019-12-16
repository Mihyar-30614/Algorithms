import sys
# Initialize Variables
ARRAY_SIZE = 1000001
S = ['BLANK'] * ARRAY_SIZE
S[1] = 'HAPPY'

P = [0] * ARRAY_SIZE
P[1] = 1

# Inspired by https://www.javatpoint.com/python-program-to-check-if-the-given-number-is-happy-number
def isHappy(j):
    remain = sum = 0
    while(j > 0):
        remain = j % 10
        sum = sum + (remain * remain)
        j = j // 10
    return sum


def checkStatus(index):

    if S[index] == "HAPPY":
        return "HAPPY"
    elif S[index] == "UNHAPPY" or S[index] == "WAITING":
        return "UNHAPPY"
    else:
        j = isHappy(index)
        S[index] = "WAITING"
        retval = checkStatus(j)
        S[index] = retval
        return retval


for i in range(1, ARRAY_SIZE):
    result = checkStatus(i)
    
    if result == "HAPPY":
        P[i] = P[i-1] + 1
    else:
        P[i] = P[i-1] + 0


T = int(sys.stdin.readline())
for i in range(T):
    line = sys.stdin.readline().split()
    A = int(line[0])
    B = int(line[1])
    print(P[B] - P[A-1])
