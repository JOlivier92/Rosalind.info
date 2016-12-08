#!/usr/bin/env python3
# Name: Joseph Olivier


class FileReader:
	#Completely unneccessary filereader...
	def __init__(self,file):
		self.file = file
	def reader(self):
		for line in self.file:
			return line.strip()
def main():
	import sys
	uniprotID = FileReader(sys.stdin).reader()
	findProcesses(uniprotID)

def findProcesses(uniprotID):
	from Bio import ExPASy
	from Bio import SwissProt
	#If you are confused, check out the biopython documentation on swissProt
	handle = ExPASy.get_sprot_raw(uniprotID)
	record = SwissProt.read(handle)
	handle.close()
	#Put the stuff we are interested in inside of a list
	crossReferenceList = record.cross_references
	GOList = [i for i in crossReferenceList if i[0]=="GO"]
	GOList = [i for i in GOList if i[2].startswith("P")]
	for i in range(0,len(GOList)):
		currentGOinfo = GOList[i]
		#Info we are looking for
		actualInfo = currentGOinfo[2]
		#Strip leading symbols
		print(actualInfo[2:])

main()
