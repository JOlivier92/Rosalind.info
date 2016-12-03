#!/usr/bin/env Python
# Name: Joseph Olivier
with open("rosalind_subs.txt", "r") as inputfile:
	sequence = inputfile.readline().upper().strip()
	substring = inputfile.readline().upper().strip()
x = len(substring)
y = len(sequence)
def compare(sequence,substring,x,y):
	z = 1
	count = 0
	print(sequence,y)
	print(substring,x)
	while z < y:
		if substring == sequence[z:(z+x)]:
			count += 1
			print(z+1,end=" ")
		z += 1
	return count
print(compare(sequence,substring,x,y))
