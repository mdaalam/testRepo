# Name: Md Alam
# Id: 106976395

import sys
import os

file = sys.argv[1]

# open input file, read only and universal newline support, and read in data
data = open(sys.argv[1],'rU').read()

# split rows by newlines and columns by tabs, and represent as list of lists
rows = [line.split('\t') for line in data.split('\n')]

# This method return the number of rows of the file
def countRows():
    lines = 0
    for line in open(file):
        lines += 1
    return lines

# This method returns the number of columns of the file
def countColumn():
	tabs = 0
	for line in open(file):
 		tabs += line.count('\t')
 		break
 	return tabs+1

# This method determine if any value is missing on the file
def determineColumns():
	tabs = 0
	for line in open(file):
		tabs += line.count('\t')
		break
	for line in open(file):
		if (line.count('\t') < tabs):
			print "Cannot determine number of columns"
			sys.exit(0)

# This method returns the first rows (heading) of the file
def findHeading():
	tabs = 0
	for line in open(file):
		print(data.split('\t'))
 		tabs += line.count('\t')
 		print tabs
 		break
    
# This method print all the rows of a specific column
def printColumn(i):
	a = []
	for line in open(file):
		columns = line.split('\t')
		if len(columns) >= i:
			a.append(columns[i])
	print "Column ", i, ": ", a.pop(0)
	print "-------------------------------"
	#a.sort()
	#length = len(a)

	# Convert String to int if needed
	count = 0
	for i in a:
		if (a[count].isdigit()):
			a[count] = int(a[count])
			count += 1
		
	b = list(set(a))

	# Sorting the list
	b.sort()

	# Counting and Eleminating duplicate, then print
	for i in b:
		count = 0
		for j in a:
			if (i == j):
				count += 1
		print count, "\t",

		#if a != b:
		print(i)		

# This method print all data using required format
def printData():
	for i in range(countColumn()):
		print "-------------------------------" 
		printColumn(i)
	
print "Attempting to open input.txt..... Success!"
print "Number of rows:", countRows()
determineColumns()
print "Number of columns:", countColumn()
#findHeading()
#print(rows)
printData()
