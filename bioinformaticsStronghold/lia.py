#!/usr/bin/env python3
# Name: Joseph Olivier

class IndependentAlleles:
	def __init__(self,k,N):
		#kth generation
		#N individuals with Aa Bb haplotype
		self.k = int(k)
		self.N = int(N)
		self.totalKids = 2**self.k
		self.probability = 0

	def counter(self):
		#Importing built-in math module for factorial.
		import math
		#for i in range starting from least amount of kids with AaBb to max(all) amount of kids with AaBb
		for i in range(self.N,self.totalKids+1):
			#Add probability for certain i.
			#Probability for i == 1/4^i * 3/4^(total-i) * totalCi
			self.probability+=0.25**(i)*0.75**(self.totalKids-i)*(math.factorial(self.totalKids)/(math.factorial(i)*math.factorial(self.totalKids-i)))
		return self.probability







class FileReader:
	#Simple file reader. Reads in 2 integers separated by a space.
	#returns 2 integers (k and N)
	def __init__(self,file):
		self.file = file
	def reader(self):
		kN = list()
		for line in self.file:
			kN = line.split(" ")
		return kN[0],kN[1]
def main():
	import sys
	findkN = FileReader(sys.stdin)
	k,N = findkN.reader()
	iAlleles = IndependentAlleles(k,N)
	print(iAlleles.counter())
main()