#!/usr/bin/env python3
# Name: Joseph Olivier
#Very very ugly code :(
#Much more succint ways to do this once you look at the solutions for this problem on rosalind.
class Assembler:
	def __init__(self,sequenceList):
		self.sequenceList = sequenceList
		self.halfLength = int()
		self.endSequence = str()
		self.listofMatches = list()
		self.organizedList = list()

	def mainController(self):
		self.findMatch()
		#Add first item to the organized list as a starting point.
		#Organize nodes in order.
		self.currentMatch = self.listofMatches[0]
		self.organizedList.append(self.currentMatch)
		#Calls organize to front after endNode is found
		self.organizeToEnd()
	
	def findMatch(self):
		for i in range(0,len(self.sequenceList)):
			self.halfLength = round(len(self.sequenceList[i])/2)
			currentSequence = self.sequenceList[i]
			for j in range(0,len(self.sequenceList)):
				if j == i:
					pass
				else:
					checkedSequence = self.sequenceList[j]
					if currentSequence[-self.halfLength:] in checkedSequence:
						self.listofMatches.append((i,j))
					else:
						self.endSequence+=currentSequence
	
	def organizeToEnd(self):
		for matchedTuple in self.organizedList[-1:]:
			for item in self.listofMatches:
				if matchedTuple[1] == item[0]:
					self.organizedList.append(item)
					break
				elif item == self.listofMatches[-1]:
					self.organizeToFront()

				else:
					pass
		self.organizeToEnd()
	
	def organizeToFront(self):
		matchedTuple = self.organizedList[0]
		for item in self.listofMatches:
			if matchedTuple[0] == item[1]:
				self.organizedList.insert(0,item)
				break
			elif item == self.listofMatches[-1]:
				self.concatenateResults()
			else:
				pass
		self.organizeToFront()

	def concatenateResults(self):
		import sys
		concatedString = str()
		for i in range(0,len(self.organizedList)):
			currentEdge = self.organizedList[i]
			sourceNode = self.sequenceList[currentEdge[0]]
			sinkNode = self.sequenceList[currentEdge[1]]
			if i == 0:
				self.halfLength = round(len(sourceNode)/2)
			self.checkBiggerMatch(sourceNode,sinkNode)
			copyMe = len(sinkNode)
			sinkNode = sinkNode.replace(sourceNode[-self.halfLength:],"")
			if i == 0:
				concatedString+=sourceNode
			concatedString+=sinkNode
			self.halfLength = round(copyMe/2)+1
			
		print(concatedString)
		sys.exit()
	
	def checkBiggerMatch(self,sourceNode,sinkNode):
		self.halfLength+=1
		if sourceNode[-self.halfLength:] in sinkNode:
			self.checkBiggerMatch(sourceNode,sinkNode)
		else:
			self.halfLength-=1

class FileReader:
	def __init__(self,file):
		self.file = file
		self.sequenceIDList = list()
		self.sequenceList = list()

	def reader(self):
		for line in self.file:
			if line.startswith(">"):
				if self.sequenceIDList:
					self.sequenceList.append(currentSequence)
				self.sequenceIDList.append(line.rstrip())
				currentSequence = str()
			else:
				currentSequence+=line.rstrip().upper()
		self.sequenceList.append(currentSequence)
		return self.sequenceIDList,self.sequenceList

def main():
	import sys
	fastaReader = FileReader(sys.stdin)
	sequenceIDList,sequenceList = fastaReader.reader()
	assembly = Assembler(sequenceList)
	print(assembly.mainController())
main()
