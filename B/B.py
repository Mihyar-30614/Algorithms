import sys

# Read the first line
T = int(sys.stdin.readline())
for i in range(T):
    line = sys.stdin.readline();
    binary = bin(int(line) + 1);
    index = binary.index('1');
    print(binary[index+1:]);