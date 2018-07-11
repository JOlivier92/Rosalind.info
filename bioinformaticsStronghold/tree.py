#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Completing a Tree
# Hyperlink http://rosalind.info/problems/tree/


class GenerateTree:

	def __init__(self,listofEdges,listofUnconnectedNodes):
		self.edges = listofEdges
		self.listofBranches = []
		self.unconnectedNodes = listofUnconnectedNodes

	def classController(self):
		numberofNeededNodes,listofBranches = self.makeBranches()
		return numberofNeededNodes

	def makeBranches(self):
		currentBranch = [self.edges[0][0],self.edges[0][1]]
		indicesofBranch = [0]
		counter = 1

		while counter < len(self.edges):
			if self.edges[counter][0] in currentBranch and counter not in indicesofBranch:
				currentBranch.append(self.edges[counter][1])
				indicesofBranch.append(counter)
				counter = 0
			elif self.edges[counter][1] in currentBranch and counter not in indicesofBranch:
				currentBranch.append(self.edges[counter][0])
				indicesofBranch.append(counter)
				counter = 0
			else:
				counter+=1

		self.listofBranches.append(currentBranch)		
		
		indicesofBranch = sorted(indicesofBranch,reverse=True)
		for i in range(0,len(indicesofBranch)):
			self.edges.pop(indicesofBranch[i])

		if len(self.edges) >= 1:
			self.makeBranches()
			
		return len(self.listofBranches)-1+len(self.unconnectedNodes),self.listofBranches



class FileReader:
	def __init__(self,filetoRead):
		self.file = filetoRead

	def reader(self):
		edges = []
		n = int(self.file.readline())
		allNodes = [x for x in range(1,n+1)]
		listofConnectedNodes = []

		
		for line in self.file:
			edges.append([int(x) for x in line.strip().split(" ")])
			for edge in edges[-1]:
				listofConnectedNodes.append(edge)
				
		unconnectedNodes = [x for x in allNodes if x not in listofConnectedNodes]

		return edges,unconnectedNodes

def main():
	import sys
	edges,unconnectedNodes = FileReader(sys.stdin).reader()
	numberofNeededNodes = GenerateTree(edges,unconnectedNodes).classController()
	print(numberofNeededNodes)

main()