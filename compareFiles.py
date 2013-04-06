#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/4/2013

#Outputs the difference between 2 directories, purposely ignoring file placement
#Uses partial match for title based off a character sum
#	and uses perfect matching for file size to confirm matching

#Purpose: Allow an amount of tolerance of difference between file names
#	while ensuring same file size

import os
import sys

def stringSum(string):
	string = string.upper().replace('.', ' ')[:10]
	total = 0
	for char in string:
		total += ord(char)
	return total

def dirWalker(dirList,root,base):
	print('Searching %s\\'%root)
	os.chdir(root)
	for item in os.listdir():
		if os.path.isfile(item):
			total = stringSum(item)+os.stat(item).st_size
			while total in dirList:
				total += 0.1
			dirList[total]=[item, os.stat(item).st_size]
	for item in os.listdir():
		if os.path.isdir(item):
			dirWalker(dirList,item,base)
			os.chdir('..')
	return

if __name__ == '__main__':
	outputToFile = False
	
	if len(sys.argv) == 3:
		print('Outputting to Terminal\n')
	elif len(sys.argv) == 4:
		outputFile = sys.argv[3]
		outputToFile = True
	else:
		print('Usage: "python compareFiles.py comparepath\\\\to\\\\directory\\\\1 path\\\\to\\\\directory\\\\2"')
		print('OR')
		print('Usage: "python compareFiles.py comparepath\\\\to\\\\directory\\\\1 path\\\\to\\\\directory\\\\2 outputFileName.txt"')
		exit()
		
	if not os.path.isdir(sys.argv[1]):
		print('%s is not a valid directory'%sys.argv[1])
		exit()
	if not os.path.isdir(sys.argv[2]):
		print('%s is not a valid directory'%sys.argv[2])
		exit()
	
	print('Comparing %s and %s'%(sys.argv[1],sys.argv[2]))
	print('------------------------------------------')
	
	d1 = {}
	dirWalker(d1,sys.argv[1],sys.argv[1])	
	print()
	d2 = {}
	dirWalker(d2,sys.argv[2],sys.argv[2])
	d1Unique = []
	d2Unique = []
	print()
	
	for item in d1.keys():
		#print('Comparing %s key %s'%(d1[item][0],item))
		match = False
		for item2 in d2.keys():
			if item > item2 -32 and item < item2+32:
				if d1[item][1] == d2[item2][1]:
					#print('Matches: %s key %s'%(d2[item2][0],item2))
					match = True
		if not match:
			d1Unique.append(d1[item][0])
			#print('%s ........ key %s size %s'%(d1[item][0],item,d1[item][1]))
	
	for item2 in d2.keys():
		#print('Comparing %s key %s'%(d2[item2][0],item2))
		match = False
		for item in d1.keys():
			if item2 > item -32 and item2 < item+32:
				if d1[item][1] == d2[item2][1]:
					#print('Matches: %s key %s'%(d1[item][0],item))
					match = True
		if not match:
			d2Unique.append(d2[item2][0])
			#print('%s ........ key %s size %s'%(d2[item2][0],item2,d2[item2][1]))
			
	if outputToFile:
		output = open(outputFile,'w')
		output.write('Items Unique to %s:\n'%sys.argv[1])
		for item in d1Unique:
			output.write('%s\n'%item)
		output.write('\n')
		output.write('Items Unique to %s:\n'%sys.argv[2])
		for item in d2Unique:
			output.write('%s\n'%item)
		output.write('\n')
		
		output.close()
		
		print('File \'%s\' successfully written in %s...'%(sys.argv[3],sys.argv[2]))
	else:
		print('Items Unique to %s:'%sys.argv[1])
		for item in d1Unique:
			print(item)
		print()
		print('Items Unique to %s:'%sys.argv[2])
		for item in d2Unique:
			print(item)
