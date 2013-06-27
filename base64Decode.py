import sys

inputString = raw_input()

base64Index = {'+':62,'/':63}

#Uppercase letters
index = 65
for num in range(0,26):
	base64Index[chr(index)] = num
	index +=1

#Lowercase letters
index = 97
for num in range(26,52):
	base64Index[chr(index)] = num
	index +=1

#Numbers
index = 48
for num in range(52,62):
	base64Index[chr(index)] = num
	index +=1

binString = ''

for char in inputString:
	if char == '=':
		break
	current = bin(base64Index[char])[2:]
	while len(current)<6:
		current = '0'+current
	binString+=current
	
	
while len(binString) >=8:
	current = binString[:8]
	ascii = int(current, 2)
	sys.stdout.write(chr(ascii))
	binString = binString[8:]

print

