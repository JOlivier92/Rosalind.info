#!/usr/bin/env python3
# Name: Joseph Olivier

class FileReader:
	def __init__(self,file):
		self.file = file
	def reader(self):
		sequence = str()
		for line in self.file:
			sequence+=line.upper().rstrip()
		return sequence
def main():
	import sys
	sequence = FileReader(sys.stdin).reader()
	counter(sequence)

def counter(sequence):
	#print the count of each nucleotide followed by a space.
	print(sequence.count("A"),end=" ")
	print(sequence.count("C"),end=" ")
	print(sequence.count("G"),end=" ")
	print(sequence.count("T"))	

main()

