#!/usr/bin/env python3
# Name: Joseph Olivier
# Rosalind Problem: Searching Through the Haystack 
# Hyperlink http://rosalind.info/problems/lcsm/


class FindSharedMotif:
	def __init__(self,listofSequences):
		self.sequences = listofSequences
		self.subStrings = []
		self.optimizedCheckStrings = []

	def classController(self):
		self.optimizeSearch()
		for i in range(1,len(self.sequences)):
			self.findMatchedSubStrings(self.sequences[i].upper())
		
		return self.optimizedCheckStrings

	def optimizeSearch(self):
		import sys
		for i in range(0,len(self.sequences[0].upper())-1):
			for j in range(i+1,len(self.sequences[0].upper())):
				self.optimizedCheckStrings.append(self.sequences[0].upper()[i:j+1])

		self.optimizedCheckStrings = list(set(self.optimizedCheckStrings))

	def findMatchedSubStrings(self,currentSequence):
		import sys
		removeList = []
		newList = []
		for subSequence in self.optimizedCheckStrings:
			if subSequence in currentSequence:
				pass
			else:
				print("subsequence " + subSequence+" not found in "+ currentSequence," removing " + subSequence)
				removeList.append(subSequence)
		print(len(self.optimizedCheckStrings),len(removeList))
		for item in self.optimizedCheckStrings:
			if item in removeList:
				pass
			else:
				newList.append(item)
		self.optimizedCheckStrings = [x for x in newList]

	def removeSubstring(self,sequence):
		while sequence in self.optimizedCheckStrings:
			print(sequence)
			self.optimizedCheckStrings.remove(sequence)


class FileReader:
	def __init__(self,filename):
		self.filename = filename

	def reader(self):
		i = 0
		sequences = []
		for line in self.filename:
			if i % 2 == 0:
				pass
			else:
				sequences.append(line.strip())
			i+=1
		return sequences



def main():
	import sys
	readInput = FileReader(sys.stdin)
	listofSequences = readInput.reader()
	x = FindSharedMotif(listofSequences).classController()
	print(x)


main()