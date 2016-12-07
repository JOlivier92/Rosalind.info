#!/usr/bin/env python3
# Name: Joseph Olivier

class TransversionFinder:
	def __init__(self,sequenceList):
		#convert both sequences to lists for enumeration
		self.masterSequence = list(sequenceList[0])
		self.pairwiseSequence = list(sequenceList[1])
		self.purines = "AG"
		self.pyrimidines = "TC"
		self.transitions = 0
		self.transversions = 0

	def pairNucleotides(self):
		#loop through each position in each sequence.
		#Send tuple of symbols to find tranversions function
		for i in range(0,len(self.masterSequence)):
			self.findTransversions((self.masterSequence[i],self.pairwiseSequence[i]))
		
		print(self.transitions/self.transversions)

	def findTransversions(self,tpleOfNucleotides):
		#If the nucleotides are the same, do nothing
		if tpleOfNucleotides[0] == tpleOfNucleotides[1]:
			pass
		#Otherwise, do something
		#If symbol[0] is a purine, check if symbol [1] is a purine or pyramidine.
		elif tpleOfNucleotides[0] in self.purines:
			#If pyrimidine, add 1 to transversions
			if tpleOfNucleotides[1] in self.pyrimidines:
				self.transversions+=1
			#Otherwise, add 1 to transitions
			else:
				self.transitions+=1
		#Else (symbol[0] is pyrimidine), check symbol [1] again and add to
		#transversions or transitions accordingly.
		else:
			if tpleOfNucleotides[1] in self.purines:
				self.transversions+=1
			else:
				self.transitions+=1

class FileReader:
	def __init__(self,file):
		self.file = file
		self.sequenceIDList = list()
		self.sequenceList = list()

	def reader(self):
		currentSequence = str()
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
	readFasta = FileReader(sys.stdin)
	sequenceList,sequenceIDList = readFasta.reader()
	calculateTrans = TransversionFinder(sequenceList)
	calculateTrans.pairNucleotides()

main()