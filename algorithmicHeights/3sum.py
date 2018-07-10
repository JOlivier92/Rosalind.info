#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: 3sum
# Hyperlink http://rosalind.info/problems/3sum/


class FileReader:

	def __init__(self,filetoRead):
		self.file = filetoRead

	def reader(self):
		self.file.readline()
		arrays = []
		for line in self.file:
			arrays.append([int(x) for x in line.split()])
		return arrays

def find_sum_of_parts(array):
	startingArray = array[:]
	array.sort()
	for i in range(0,len(array)-2):
		a = array[i]
		j = i+1
		k = len(array)-1
		while j < k:
			b = array[j]
			c = array[k]
			if a+b+c == 0:
				return sorted([startingArray.index(a)+1,
							   startingArray.index(b)+1,
							   startingArray.index(c)+1])
			elif a+b+c > 0:
				k-=1
			else:
				j+=1
	return [-1]

def main():
	import sys
	inputArrays = FileReader(sys.stdin).reader()
	output = []
	for array in inputArrays:
		output.append(find_sum_of_parts(array))
	for i in range(0,len(output)):
		if len(output[i]) > 1:
			print(output[i][0],end=" ")
			print(output[i][1],end=" ")
			print(output[i][2])
		else:
			print(output[i][0])
main()
#credit to sefakilic on github. her succinct solution really helped me work through my own solution
#which had time complexity issues. 