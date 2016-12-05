#!/usr/bin/env python3
# Name: Joseph Olivier


class GCChecker:
	def __init__(self,sequence,probability):
		self.sequence = sequence.upper()
		self.probabilityofGorC = float(probability)/2
		self.probabilityofAorT = (1-float(probability))/2

	def positionalProbability(self):
		import sys
		import math
		logProbabilty = 0
		#Go through each character in the sequence
		for i in range(0,len(self.sequence)):
			#If the character is an A or a T, then add log10Probability(AorT) to logProbability
			if self.sequence[i] in "AT":
				logProbabilty+=math.log10(self.probabilityofAorT)
			#else, then add log10Probability(GorC) to logProbability
			else:
				logProbabilty+=math.log10(self.probabilityofGorC)	
		return logProbabilty

class FileReader:
	#Simple file reader. 
	def __init__(self,file):
		self.file = file
		self.sequence = str()
		self.probabilityList = list()
	def makeLists(self):
		counter = 0
		for line in self.file:
			if counter == 0:
				self.sequence = line.rstrip()
				counter+=1
			else:
				self.probabilityList = line.rstrip().split(" ")
		return self.sequence,self.probabilityList

def main():
	import sys
	outputList = list()
	reader = FileReader(sys.stdin)
	sequence,probabilityList = reader.makeLists()
	#Goes through each GC probability in the probability array 1 by 1.
	for i in range(0,len(probabilityList)):
		findLogProbability = GCChecker(sequence,probabilityList[i])
		outputList.append(findLogProbability.positionalProbability())
	#Print out each item separated by a space
	#{}.format is float formatting to go to 3 characters after the .
	for item in outputList:
		print("{0:.3f}".format(item),end=" ")
	print("\n")

main()