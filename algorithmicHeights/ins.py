#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Insertion Sort
# Hyperlink http://rosalind.info/problems/ins/

class FileReader:

	def __init__(self,filetoRead):
		self.file = filetoRead
	def reader(self):
		self.file.readline()
		return [int(x) for x in self.file.readline().split()]

def insertionSort(listtoSort):
	numberofSteps = 0
	for i in range(1,len(listtoSort)):
		while listtoSort[i] < listtoSort[i-1] and i >= 1:
			a = listtoSort[i]
			listtoSort[i] = listtoSort[i-1]
			listtoSort[i-1] = a
			i-=1
			numberofSteps+=1
	return listtoSort,numberofSteps


def main():
	import sys
	inputData = FileReader(sys.stdin).reader()
	sortedList,numberofSteps = insertionSort(inputData)
	print(numberofSteps)

main()