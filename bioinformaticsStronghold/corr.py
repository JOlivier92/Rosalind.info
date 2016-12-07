#!/usr/bin/env python3
# Name: Joseph Olivier


class ErrorCorrectionReads:
	def __init__(self,sequenceList):
		self.sequenceList = sequenceList
		self.reverseComplement = list()
		self.correctSequences = list()
	
	def mainController(self):
		#Call all functions in order
		self.reverseComplementer()
		self.checkMatch()
		self.similarityChecker()
	def reverseComplementer(self):
		complement = {"A":"T","G":"C","C":"G","T":"A"}
		for sequence in self.sequenceList:
			nucleotides = list(sequence)
			nucleotides = [complement[nucleotide] for nucleotide in nucleotides]
			newSequence = "".join(nucleotides[::-1])
			self.reverseComplement.append(newSequence)

	def checkMatch(self):
		#Remove any repeats in the sequence list
		matchedSequences = list()
		for i in range(0,len(self.sequenceList)):
			if self.sequenceList[i] in self.sequenceList[i+1:] or self.sequenceList[i] in self.reverseComplement[i+1:]:
				matchedSequences.append(i)
		#Add correctSequences to that list, delete correct sequences from list to check in similarity checker
		for item in matchedSequences[::-1]:
			self.correctSequences.append(self.sequenceList[item])
			self.correctSequences.append(self.reverseComplement[item])
			del self.sequenceList[item]
	
	def similarityChecker(self):
		#For each sequence in the sequenceList of items that are imperfect
		for i in range(0,len(self.sequenceList)):
			#Check against each perfect sequence
			for j in range(0,len(self.correctSequences)):
				#See if hamming distance is one. If so, print it, then go to next sequence in sequenceList (break)
				if sum(i != j for i,j in zip(self.sequenceList[i],self.correctSequences[j])) == 1:
					print(self.sequenceList[i] + "->" + self.correctSequences[j])
					break

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
	correctErrors = ErrorCorrectionReads(sequenceList)
	correctErrors.mainController()
main()