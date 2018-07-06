#!/usr/bin/env python3
# Name: Joseph Olivier
# Rosalind Problem: Searching Through the Haystack 
# Hyperlink http://rosalind.info/problems/lcsm/


class FindSharedMotif:
	def __init__(self,sequences):
		self.sequences = sequences
		self.commonSubStrings = []
	
	def classController(self):
		self.optimizer()
		self.compare_each_string()
		longestSequence = self.find_longest_word()
		return longestSequence

	def optimizer(self):
		"""
		Attempts to optimize this problem by first looking at all common substrings
		of the first 2 sequences of the dataset. Then, it sorts the common substrings
		by descending length (In a truly random world, it is less likely that the longer
		substrings will be common, therefore if we search by descending length we can more
		quickly reduce the length of the commonSubString list, improving the search over time!)
		"""
		import sys

		for i in range(0,len(self.sequences[0])-1):
			for j in range(i+1,len(self.sequences[0])):
				if self.sequences[0][i:j] in self.sequences[1]:
					self.commonSubStrings.append(self.sequences[0][i:j])
		self.commonSubStrings = list(set(self.commonSubStrings))
		self.commonSubStrings.sort(key=len,reverse=True)

	def compare_each_string(self):
		removeList = []
		for i in range(2,len(self.sequences)):
			for j in range(0,len(self.commonSubStrings)):
				if self.commonSubStrings[j] not in self.sequences[i]:
					removeList.append(self.commonSubStrings[j])
			self.commonSubStrings = [x for x in self.commonSubStrings if x not in removeList]
					
	def find_longest_word(self):
		longestSequence = ""
		for i in range(0,len(self.commonSubStrings)):
			if len(self.commonSubStrings[i]) > len(longestSequence):
				longestSequence = self.commonSubStrings[i]
		return longestSequence

class FileReader:
	def __init__(self,file):
		self.file = file
	
	def reader(self):

		sequences = []
		currentSequence = ""
		for line in self.file:
			if line.startswith(">"):
				if currentSequence:
					sequences.append(currentSequence)
					currentSequence = ""
			else:
				currentSequence+=line.strip()
		return sequences
def main():
	import sys
	readInput = FileReader(sys.stdin)
	listofSequences = readInput.reader()
	x = FindSharedMotif(listofSequences).classController()
	print(x)

main()