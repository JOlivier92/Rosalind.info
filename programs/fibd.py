#!/usr/bin/env python3
# Name: Joseph Olivier


class RabbitCounter:
	#n = number of months in simulation
	#m = lifespan of rabbit
	#babypairs optional arg if you want to change the amount of starting pairs.
	#Deathlist keeps track of the lifespan of the rabbits.
	def __init__(self,n,m,babypairs=1):
		import numpy as np
		self.n = int(n)
		self.m = int(m)
		self.babypairs = babypairs
		self.adultpairs = 0
		self.deathlist = [0]*int(self.m)
	def rabbitCounter(self):
		#Modifies the deathlist to start at month 3.
		self.deathlist[2] = 1
		self.deathlist[0] = 1
		for i in range(2,self.n+1):
			#producing parents are the parents that were alive after the previous iteration
			#number of babypairs to adulthood is the number of babyrabbits from previous iteration
			producingParents = self.adultpairs
			toAdultHood = self.babypairs
			if i <= 3:
				self.adultpairs+=toAdultHood
				self.babypairs-=toAdultHood
				self.babypairs+=producingParents
			else:
				#subtract the rabbits who have lived long enough :(
				#add rabbits who were previously babies
				self.adultpairs-=self.deathlist[self.m-1]
				self.adultpairs+=toAdultHood
				#Adds a pair per producing pair of parents. Subtract the ones who became adults
				self.babypairs+=producingParents
				self.babypairs-=toAdultHood
				#Change the deathlist. Each index == the previous index.
				#For example, index 1 corresponds to how many rabbits have been alive for 2 months,
				#Change that number to the number of rabbits which were previously alive for 1 month.
				for j in range(1,self.m+1):
					self.deathlist[self.m-j] = self.deathlist[self.m-j-1]
				self.deathlist[0] = producingParents
				
		return self.adultpairs+self.babypairs



class FileReader:
	#Simple file reader. Reads in 2 integers separated by a space.
	#returns 2 integers (n and m)
	def __init__(self,file):
		self.file = file
	def reader(self):
		nm = list()
		for line in self.file:
			nm = line.split(" ")
		return nm[0],nm[1]
def main():
	import sys
	findNM = FileReader(sys.stdin)
	n,m = findNM.reader()
	countRabbits = RabbitCounter(n,m)
	print(countRabbits.rabbitCounter())
main()