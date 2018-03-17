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
		print("hi",len(self.sequences))
		self.optimizeSearch()
		for i in range(2,len(self.sequences)):
			self.findMatchedSubStrings(self.sequences[i].upper())
		return self.optimizedCheckStrings

	def optimizeSearch(self):
		import sys
		tempString1Sequences = []
		tempString2Sequences = []
		tempString2 = []
		firstString = self.sequences[0].upper()
		secondString = self.sequences[1].upper()
		print(firstString)
		for i in range(0,len(firstString)-1):
			print(firstString[i],i)
			for j in range(i+1,len(firstString)):
				print(i,j)
				if firstString[i:j+1] not in tempString1Sequences:
					if j == len(firstString)-1:
						self.optimizedCheckStrings.append(firstString[i:])
					else:
						self.optimizedCheckStrings.append(firstString[i:j+1])
		#self.optimizedCheckStrings = tempString1Sequences
		# for i in range(0,len(secondString)-1):
		# 	for j in range(i+1,len(secondString)):
		# 		if secondString[i:j+1] not in tempString2Sequences:
		# 			if j == len(secondString)-1:
		# 				tempString2Sequences.append(secondString[i:])
		# 			else:
		# 				tempString2Sequences.append(secondString[i:j+1])

		# self.optimizedCheckStrings = [x for x in tempString1Sequences if x in tempString2Sequences]
		# self.optimizedCheckStrings.append("A")
		print(self.optimizedCheckStrings)

	def findMatchedSubStrings(self,currentSequence):
		import sys
		for subSequence in self.optimizedCheckStrings:
			print(subSequence)
			if subSequence in currentSequence:
				print("yup",subSequence,currentSequence)
				pass
			else:
				print("nope")
				self.removeSubstring(subSequence)
	def removeSubstring(sequence):
		while sequence in self.optimizedCheckStrings:
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