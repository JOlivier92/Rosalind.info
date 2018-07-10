#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: 2SUM
# Hyperlink http://rosalind.info/problems/2sum/



class FileReader:

	def __init__(self,filetoRead):
		self.file = filetoRead

	def reader(self):
		arrays = []
		self.file.readline()

		for line in self.file:
			arrays.append([int(x) for x in line.split()])

		return arrays

def findMatchingNumbers(listofArrays):
	import math
	outputIndices = []
	arrayLength = len(listofArrays[0])
	for array in listofArrays:
		for i in range(0,math.ceil(arrayLength/2)+1):
			if -array[i] in array and array[i] != 0:
				outputIndices.append([i+1,array.index(-array[i])+1])
				break
			elif array[i] == 0:
				if 0 in array[i+1:]:
					outputIndices.append([i+1,array[i+1:].index(0)+i+2])
					break
			if i == math.ceil(arrayLength/2-1):
				outputIndices.append(-1)

	return outputIndices


def main():
	import sys
	inputArrays = FileReader(sys.stdin).reader()
	outputIndices = findMatchingNumbers(inputArrays)
	for index in outputIndices:
		if type(index) is list:
			print(index[0],index[1])
		else:
			print(index)

main()