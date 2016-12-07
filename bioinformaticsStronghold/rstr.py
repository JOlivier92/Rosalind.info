#!/usr/bin/env python3
# Name: Joseph Olivier

class MatchingStrings:
	def __init__(self,variables):
		self.x = variables[0]
		self.N = variables[1]
		self.sequence = variables[2]
		self.probabilityofGorC = float(self.x)/2
		self.probabilityofAorT = (1-float(self.x))/2
	
	def probabilityCaclculator(self):
		probability = 1
		#Calculate the probability of the sequence occuring given the GC cotent
		for i in range(0,len(self.sequence)):
			if self.sequence[i] in "AT":
				probability*=self.probabilityofAorT
			else:
				probability*=self.probabilityofGorC
		#Calculate the probability of the sequence NEVER occuring over N trials...
		#Subtract that probability from 1 to see what the probability of it occuring 1 or more times is.
		print(1-(1-probability)**int(self.N))


class FileReader:
	def __init__(self,file):
		self.file = file
	def reader(self):
		xandN = self.file.readline()
		sequence = self.file.readline().rstrip().upper()
		xandN = xandN.rstrip().split(" ")
		x = xandN[1]
		N = xandN[0]
		return x,N,sequence
def main():
	import sys
	variables = FileReader(sys.stdin).reader()
	print(variables)
	matcher = MatchingStrings(variables)
	matcher.probabilityCaclculator()
main()