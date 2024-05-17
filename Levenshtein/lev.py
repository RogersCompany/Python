from Levenshtein import distance as lev
import sys

# Using readlines()
file1 = open('pli07.txt', 'r')
Lines = file1.readlines() 
strToMatch = sys.argv[1]
number=int(sys.argv[2])

for line in Lines:
	string = line.strip()
	x = lev(strToMatch, string)
	if x <= number:
		print(x)
		print(line)

file1.close()
