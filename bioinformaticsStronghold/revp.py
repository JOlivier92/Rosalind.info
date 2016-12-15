#!/usr/bin/env python3
# Name: Joseph Olivier
class ReverseFinder:
	def __init__(self,sequence):
		self.sequence = list(sequence)
		self.reverseTuples = [("A","T"),("C","G")]
		self.listofPalindromes = list()
	
	def classController(self):
		self.checkforPalindrome()

		#Passes index+1,4mer to next function
		#self.listofPalindromes.sort(key=lambda tup: tup[0])
		for item in self.listofPalindromes:
			self.checkPlus2(item)
		
		self.outputPrinter()
	def checkforPalindrome(self):
		#Checks each index to see if a 4mer Palindrome in possible. If so, send sequence to check4mer() to check
		#the inner sequence in the current 4 length sequence
		for i in range(0,len(self.sequence)-3):
			if self.sequence[i] in self.reverseTuples[0]:
				if self.sequence[i+3] in self.reverseTuples[0] and self.sequence[i+3] != self.sequence[i]:
					self.check4mer(i,self.sequence[i:i+4])
			elif self.sequence[i] in self.reverseTuples[1]:
				if self.sequence[i+3] in self.reverseTuples[1] and self.sequence[i+3] != self.sequence[i]:
					self.check4mer(i,self.sequence[i:i+4])
			else:
				pass
	def check4mer(self,i,sequence):
		#Takes in the index and the possible 4mer palindrome.
		#If the inside of the sequence is also palindromic, add it to list of palindromes
		if sequence[1] in self.reverseTuples[0] and sequence[2] in self.reverseTuples[0]:
			if sequence[1] != sequence[2]:
				self.listofPalindromes.append((i+1,sequence))
		elif sequence[1] in self.reverseTuples[1] and sequence[2] in self.reverseTuples[1]:
			if sequence[1] != sequence[2]:
				self.listofPalindromes.append((i+1,sequence))
	def checkPlus2(self,sequenceTuple):
		#Brunt of the code in this section.
		#Takes in a sequence tuple which is the index(+1), palindromic sequece (ATAT for example)
		index = sequenceTuple[0]-1
		lengthOfCurrentPalindrome = len(sequenceTuple[1])
		#First checks to see if the sequence is at the beginning or end of the master Sequence
		if index > 0 and index < len(self.sequence)-lengthOfCurrentPalindrome:
			#Set newStart and newFinish to the 2 characters to check (on either side of the confirmed palindrome)
			newStart,newFinish = self.sequence[index-1],self.sequence[index+lengthOfCurrentPalindrome]
			#If newStart and newFinish are complements of each other, continune on
			if newStart in self.reverseTuples[0] and newFinish in self.reverseTuples[0] and newStart != newFinish:
				#Makes sure that a tuple is not added twice to our ouptut list
				if (index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]) not in self.listofPalindromes:
					self.listofPalindromes.append((index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]))
				#If the current palindrome is of length 10 or shorter, send it through this function again.
				if len(self.sequence[index-1:index+lengthOfCurrentPalindrome+1]) <= 10:
					self.checkPlus2((index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]))
			#Check above comments, this checks to see if the newStart or newFinish are C,G pairs instead of A,T pairs.
			elif newStart in self.reverseTuples[1] and newFinish in self.reverseTuples[1] and newStart != newFinish:
				if (index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]) not in self.listofPalindromes:
					self.listofPalindromes.append((index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]))
				if len(self.sequence[index-1:index+lengthOfCurrentPalindrome+1]) <= 10:
					self.checkPlus2((index,self.sequence[index-1:index+lengthOfCurrentPalindrome+1]))
			else:
				pass

	def outputPrinter(self):
		#Sorts listOfPalindromes by index for prettier output
		self.listofPalindromes.sort(key=lambda tup: tup[0])
		#Make sure to separate with a tab and not a space.
		for item in self.listofPalindromes:
			print(item[0],len(item[1]),sep="\t")
class FileReader:
	#Simple filereader which will take in a fasta formatted file.
	#For the purpose of this code, we need the first, and only, item
	#in the sequenceList.
	def __init__(self,file):
		self.file = file
		self.sequenceIDList = list()
		self.sequenceList = list()
	def reader(self):
		currentSequence = str()
		for line in self.file:
			if line.startswith(">"):
				self.sequenceIDList.append(line.rstrip())
				if currentSequence:
					self.sequenceList.append(currentSequence)
				currentSequence = str()
			else:
				currentSequence+=line.rstrip().upper()
		self.sequenceList.append(currentSequence)
		return self.sequenceList[0]
def main():
	import sys
	sequence = FileReader(sys.stdin).reader()
	ReverseFinder(sequence).classController()
main()

