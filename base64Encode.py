import sys

inputString = raw_input()

binString = ''

for char in inputString:
	ascii = bin(ord(char))[2:]
	while len(ascii) <8:
		ascii = '0'+ascii
	binString += ascii


base64Index = {62:'+',63:'/'}

#Uppercase letters
index = 65
for num in range(0,26):
	base64Index[num] = chr(index)
	index +=1

#Lowercase letters
index = 97
for num in range(26,52):
	base64Index[num] = chr(index)
	index +=1

#Numbers
index = 48
for num in range(52,62):
	base64Index[num] = chr(index)
	index +=1

count = 0
while len(binString) >=6:
	current = binString[:6]
	base64 = int(current,2)
	sys.stdout.write(base64Index[base64])
	binString = binString[6:]
	count+=1
if len(binString) >0:
	while len(binString) < 6:
		binString += '0'
	current = binString[:6]
	base64 = int(current,2)
	sys.stdout.write(base64Index[base64])
	binString = binString[6:]
	count+=1
while count%4 !=0:
	sys.stdout.write('=')
	count+=1
print
