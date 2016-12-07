#!/usr/bin/env python3
# Name: Joseph Olivier
def findPerfectMatch(sequence):
	from math import factorial
	return factorial(sequence.count("A")) * factorial(sequence.count("G"))
class FileReader:
	def __init__(self,file):
		self.file = file
		self.sequenceList = list()
		self.sequenceIDList = list()

	def readFasta(self):
		#Reads in fasta file.
		#Able to handle fasta file with multiple lines of sequences per sequenceID
		for line in self.file:
			if line.startswith(">"):
				if self.sequenceIDList:
					self.sequenceList.append(currentSequence)
				self.sequenceIDList.append(line.rstrip())
				currentSequence = str()
			else:
				currentSequence+=line.rstrip().upper()
		self.sequenceList.append(currentSequence)
		return self.sequenceList,self.sequenceIDList
def main():
	import sys
	reader = FileReader(sys.stdin)
	sequenceList,sequenceIDList = reader.readFasta()
	print(findPerfectMatch(sequenceList[0]))
main()