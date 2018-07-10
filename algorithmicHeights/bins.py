#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Binary Search
# Hyperlink http://rosalind.info/problems/bins/

class BinarySearcher:
	import sys
	def __init__(self,data):
		self.n = data[0]
		self.m = data[1]
		self.A = data[2]
		self.B = data[3]

		self.lengthofA = len(self.A)
		self.outputIndices = []

	def classController(self):
		for i in range(0,len(self.B)):
			self.binarySearcher(self.B[i],self.A)
		return self.outputIndices


	def binarySearcher(self,currentNumber,listToSearch):
		import math
		import sys

		currentList = listToSearch
		currentIndex = int(math.floor((len(listToSearch)/2)))
		if len(listToSearch) == 1:
			if currentNumber == listToSearch[0]:
				self.outputIndices.append(self.A.index(listToSearch[currentIndex])+1)
				return None
			else:
				self.outputIndices.append(-1)
				return None		
		
		if currentNumber > listToSearch[currentIndex]:
			self.binarySearcher(currentNumber,listToSearch[currentIndex:])
		elif currentNumber < listToSearch[currentIndex]:
			self.binarySearcher(currentNumber,listToSearch[:currentIndex])
		else:
			self.outputIndices.append(self.A.index(listToSearch[currentIndex])+1)
			return None

class FileReader:
	def __init__(self,filetoRead):
		self.file = filetoRead

	def reader(self):
		counter = 0 
		for line in self.file:
			if counter == 0:
				n = line.strip()
			elif counter == 1:
				m = line.strip()
			elif counter == 2:
				A = [int(x) for x in line.strip().split(" ")]
			else:
				B = [int(x) for x in line.strip().split(" ")]
			counter+=1
		return (n,m,A,B)

def main():
	import sys
	data = FileReader(sys.stdin).reader()
	output = BinarySearcher(data).classController()
	for item in output:
		print(item,end="\t")

main()

