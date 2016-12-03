#!/usr/bin/env python3
# Name: Joseph Olivier

class SequenceIDLinker:
	def __init__(self,sequenceIDList,sequenceList,O=3):
		self.sequenceList = sequenceList
		self.sequenceIDList = sequenceIDList
		#List comprehensions to create lists of the prefices and suffices of each sequence.
		#prefix list will contain characters 0,1,2
		#suffix list will contain characters -0,-1,-2
		#optional O argument to determine how big the the prefix-suffix match must be.
		self.prefixList = [x[:O] for x in sequenceList]
		self.suffixList = [x[-O:] for x in sequenceList]
		self.output = list()
	def mainController(self):
		self.checkSequence()
		self.outputPrinter()
	def checkSequence(self):
		#Go through each sequence in the fasta file.
		for i in range(0,len(self.sequenceList)):
			#If the suffix of the current sequence is the prefix for another...
			if self.suffixList[i] in self.prefixList:
				#Create a list of indices. x == index of occurence of suffix in prefix list. cannot equal curent index.
				indices = [x for x, y in enumerate(self.prefixList) if y == self.suffixList[i] and x != i]
				#Adds matches to output for printing. Tuple of source sequence to sink sequence.
				for item in indices:
					self.output.append((self.sequenceIDList[i],self.sequenceIDList[item]))
		
	def outputPrinter(self):
		for item in self.output:
			print(item[0].lstrip(">"),end=" ")
			print(item[1].lstrip(">"))
class FileReader:
	#Simple file reader. 
	#Takes in fasta file and converts to list of sequences and sequence IDs
	def __init__(self,file):
		self.file = file
		self.sequenceList = list()
		self.sequenceIDList = list()
	def makeLists(self):
		for line in self.file:
			if line.startswith(">"):
				if self.sequenceIDList:
					self.sequenceList.append(currentSequence)
				self.sequenceIDList.append(line.rstrip())
				currentSequence = str()
			else:
				currentSequence+=line.rstrip()
		self.sequenceList.append(currentSequence)
		return self.sequenceIDList,self.sequenceList
def main():
	import sys
	reader = FileReader(sys.stdin)
	sequenceIDList,sequenceList = reader.makeLists()
	linker = SequenceIDLinker(sequenceIDList,sequenceList)
	linker.mainController()
main()
