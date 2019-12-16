import sys

# Read the Number of lines
line = sys.stdin.readline().split()
N = int(line[0])
UTF = list()
Type = None
Type1 = 0
Type2 = 0
Type3 = 0
Type4 = 0
index = 0

for i in range(0, N):
	# Read the input
	Byte = sys.stdin.readline().strip()
	UTF.append(Byte)

while index < N:
	first_Byte = UTF[index]
	if first_Byte[0] == '0':
		# Type1
		Type1 += 1
		Type = 1
		index += 1
	elif first_Byte[0:3] == '110':
		# Type2
		if index+1 < N:
			second_Byte = UTF[index+1]
			if second_Byte[0:2] == '10':
				Type2 += 1
				Type = 2
				index += 2
			else:
				# Remaining Bytes doesn't match
				Type = None
				break
		else:
			# Not a complete UTF-8
			Type = None
			break
	elif first_Byte[0:4] == '1110':
		# Type3
		if index+2 < N:
			second_Byte = UTF[index+1]
			third_Byte = UTF[index+2]
			if second_Byte[0:2] == '10' and third_Byte[0:2] == '10':
				Type3 += 1
				Type = 3
				index += 3
			else:
				# Remaining bytes doesn't match
				Type = None
				break
		else:
			# Not a complete UTF-8
			Type = None
			break
	elif first_Byte[0:5] == '11110':
		# Type4
		if index+3 < N:
			second_Byte = UTF[index+1]
			third_Byte = UTF[index+2]
			forth_Byte = UTF[index+3]
			if second_Byte[0:2] == '10' and third_Byte[0:2] == '10' and forth_Byte[0:2] == '10':
				Type4 += 1
				Type = 4
				index+=4
			else:
				# Remaining bytes doesn't match
				Type = None
				break
		else:
			# Not a complete UTF-8
			Type = None
			break
	else:
		# invalid input
		Type = None
		break

if Type:
	print(Type1)
	print(Type2)
	print(Type3)
	print(Type4)
else:
	print("invalid")
