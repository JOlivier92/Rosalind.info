#!/usr/bin/env python3
# Name: Joseph Olivier


class IntronRemover:
    
    def __init__(self,sequenceList):
        self.masterSequence = sequenceList[0]
        self.Introns = sequenceList[1:]
        self.AASequence = str()
        
    def mainController(self):
        self.intronRemover()
        self.masterSequence = self.masterSequence.replace("T","U")
        #Go by 3s, insert appropriate AA into AAsequence
        for i in range(0,int(len(self.masterSequence)/3)):
            self.AASequence+=self.RNAtoAA(self.masterSequence[i*3:i*3+3])
        #Remove the terminal stop codon before returning string
        return self.AASequence.rstrip("-")
    
    def intronRemover(self):
        #Replace each intron with an empty string in the master string
        for i in range(0,len(self.Introns)):
            self.masterSequence = self.masterSequence.replace(self.Introns[i],"")

    def RNAtoAA(self,kmer):
        map_RNA = {'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
        'UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y',
        'UAC':'Y','UAA':'-','UAG':'-','UGU':'C','UGC':'C',
        'UGA':'-','UGG':'W','CUU':'L','CUC':'L','CUA':'L',
        'CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
        'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R',
        'CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I',
        'AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T',
        'ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K',
        'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V',
        'GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A',
        'GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E',
        'GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
        return map_RNA[kmer]

class FileReader:
    def __init__(self,file):
        self.file = file
        self.sequenceList = list()
    def reader(self):
        next(self.file)
        currentSequence = str()
        for line in self.file:
            if line.startswith(">"):
                self.sequenceList.append(currentSequence)
                currentSequence = str()
            else:
                currentSequence+=line.rstrip()
        self.sequenceList.append(currentSequence)
        return self.sequenceList
def main():
    import sys
    sequenceFinder = FileReader(sys.stdin)
    sequenceList = sequenceFinder.reader()
    removeIntrons = IntronRemover(sequenceList)
    print(removeIntrons.mainController())
main()
