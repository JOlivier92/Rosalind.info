#!/usr/bin/env python3
# Name: Joseph Olivier

class FileReader():
	def __init__(self,file):
		self.file = file
	def reader(self):
		for line in self.file:
			nk = line.rstrip().split(" ")
		return int(nk[0]),int(nk[1])

def main():
	import sys
	n,k = FileReader(sys.stdin).reader()
	total = 1
	#Example of 21 7
	#For i in range 1,8 (1,2,3,4,5,6,7)
	#Multiply total by currentN (21,20,19,18,17,16,15)
	#Print the total modulo 1,000,000
	for i in range(1,k+1):
		total*=n
		n-=1
		total%=1000000
	print(total)


main()
