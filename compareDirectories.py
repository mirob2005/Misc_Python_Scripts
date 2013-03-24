#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/23/2013

#Outputs the difference between 2 directories and their respective subdirectories by dirName/fileName only

import os
import sys

def dirWalker(dirList,root,base):
	print('Searching %s\\'%root)
	os.chdir(root)
	for item in os.listdir():
		if os.path.isdir(item):
			#print('%s\\'%os.path.realpath(item).replace(('%s\\')%base,''))
			dirList.append('%s\\'%os.path.realpath(item).replace(('%s\\')%base,''))
		else:
			#print('%s'%os.path.realpath(item).replace(('%s\\')%base,''))
			dirList.append('%s'%os.path.realpath(item).replace(('%s\\')%base,''))
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
		print('Usage: "python compareDirectories.py comparepath\\\\to\\\\directory\\\\1 path\\\\to\\\\directory\\\\2"')
		print('OR')
		print('Usage: "python compareDirectories.py comparepath\\\\to\\\\directory\\\\1 path\\\\to\\\\directory\\\\2 outputFileName.txt"')
		exit()
		
	if not os.path.isdir(sys.argv[1]):
		print('%s is not a valid directory'%sys.argv[1])
		exit()
	if not os.path.isdir(sys.argv[2]):
		print('%s is not a valid directory'%sys.argv[2])
		exit()
	
	print('Comparing %s and %s'%(sys.argv[1],sys.argv[2]))
	print('------------------------------------------')
	
	d1 = []
	dirWalker(d1,sys.argv[1],sys.argv[1])	
	print()
	d2 = []
	dirWalker(d2,sys.argv[2],sys.argv[2])
	d1Unique = []
	d2Unique = []
	print()
	
	for item in d1:
		if item not in d2:
			d1Unique.append(item)
	
	for item in d2:
		if item not in d1:
			d2Unique.append(item)
			
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
