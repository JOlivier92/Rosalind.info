#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Majority Element
# Hyperlink http://rosalind.info/problems/maj/

class FindMajorityElements:

	def __init__(self,inputData):
		self.k,self.n = inputData[0][0],inputData[0][1]
		self.arrays = inputData[1]

	def classController(self):
		output = []
		for i in range (0,len(self.arrays)):
			output.append(self.finder(self.arrays[i]))
		return output


	def finder(self,array):
		import math
		listofElements = {}
		halfway = int(math.ceil(len(array)/2))


		for i in range(0,len(array)):
			if array[i] in listofElements:
				listofElements[array[i]]+=1
				if listofElements[array[i]] >= halfway:
					return array[i]
			elif i > halfway:
				pass
			else:
				listofElements[array[i]] = 1
		return -1




class FileReader:
	def __init__(self,filetoRead):
		self.file = filetoRead

	def reader(self):
		variables = [int(x) for x in self.file.readline().split()]
		arrays = []
		for line in self.file:
			arrays.append([int(x) for x in line.split()])
		return [variables,arrays]
def main():
	import sys
	variablesAndArrays = FileReader(sys.stdin).reader()
	outputArray = FindMajorityElements(variablesAndArrays).classController()
	for item in outputArray:
		print(item,end="\t")
main()