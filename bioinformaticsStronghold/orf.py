#!/usr/bin/env python3
# Name: Joseph Olivier


import sys
class OpenReadingFrames:
    def __init__(self,nucleotideSequence):
        self.nucleotideSequence = nucleotideSequence[0].replace("T","U")
        self.ORF1,self.ORF2,self.ORF3 = str(),str(),str()
        self.ORF4,self.ORF5,self.ORF6 = str(),str(),str()
        self.maxLength = int()
        self.listofSequences = list()
    
    def classController(self):
        """
        This function is the class controller. It is used to run through the other functions 
        of this class.
        """
        self.ORFmaker()
        for i in range(0,len(self.ORFList)):
            self.translateORFtoAAs(self.ORFList[i],i)
        resetList = list(set(self.listofSequences))
        for item in resetList:
            print(item)
    def ORFmaker(self):
        """
        This function serves to create all of the possible Open Reading
        Frames given a sequence of DNA. It does this by setting the nucleotide
        sequence to the ORF1. ORF2/3 are created by starting 1-2 bases later.
        ORF4 is created by finding the reverse complement of ORF1. ORF5/6 are
        created in the same fashion as 2/3 using 4 as their reference.
        """
        self.ORF1 = self.nucleotideSequence
        self.ORF2 = self.ORF1[1:]
        self.ORF3 = self.ORF1[2:]
        self.ORF4 = self.reverseComplementer(self.ORF1)
        self.ORF5 = self.ORF4[1:]
        self.ORF6 = self.ORF4[2:]
        self.maxLength = len(self.ORF1)
        self.ORFList = [self.ORF1,self.ORF2,self.ORF3,
                        self.ORF4,self.ORF5,self.ORF6]
    
    def reverseComplementer(self, ORFsequence):
        """
        This function will create the reverse complement of an RNA
        string. It accomplishes this by going through each nucleotide
        in the Reversed Sequence string and appending the reverseComplement 
        string by the corresponding nucleotide.
        """
        reverseComplement = str()
        reverserDict = {"A":"U","U":"A","C":"G","G":"C"}
        reversedseq = ORFsequence[::-1]
        for nucleotide in reversedseq:
            reverseComplement+=reverserDict[nucleotide]
        return reverseComplement

    def tabletoTranslate(self,kmer):
        """
        This is the translation table which will turn a RNA
        sequence into an Amino Acid sequence.
        """
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
    
    def translateORFtoAAs(self,sequence,number):
        """
        This function will cause the ORF sequences to be turned into
        Amino Acid sequences by running them through the tabletoTranslate
        function. Then, it will push the Amino Acid Sequences through the
        main function of this class, printSequences.
        """
        AAStringfromORF = str()
        startingM = int()
        for i in range(0,len(sequence)-2,3):
            if sequence[i:i+3] != "AUG":
                pass
            else:
                startingM = i
                for i in range(startingM,len(sequence)-2,3):
                    x = self.tabletoTranslate(sequence[i:i+3])
                    AAStringfromORF+=x
                    if x == "-":
                        self.listofSequences.append(AAStringfromORF.rstrip("-").lstrip().rstrip())
                        AAStringfromORF = str()
                        break

    
class FileReader:
    """
    This filereader will take in a properly formatted file
    and create both a nucleotide string as well as an AA sequence.
    """
    def __init__(self,filename):
        self.filename = filename

    def createInputs(self):
        """
        This fileReader assumes that the file is properly formatted.
        It will concatenate all lines leading up to the last line in the file.
        The last line will be used as the AA sequence.
        """
        lineList = self.filename.readlines()
        AASequence = lineList[len(lineList)-1]
        nucleotideSequence = str()
        for line in lineList[:-1]:
            nucleotideSequence+=line.rstrip()
        return nucleotideSequence,AASequence




class FileReader:
    #Simple file reader. 
    #Takes in fasta file and converts to list of sequences and sequence IDs
    def __init__(self,file):
        self.file = file
        self.sequenceList = list()
        self.sequenceIDList = list()
    def makeLists(self):
        for line in self.file:
            if line.startswith(">"):
                if self.sequenceIDList:
                    self.sequenceList.append(currentSequence)
                self.sequenceIDList.append(line.rstrip())
                currentSequence = str()
            else:
                currentSequence+=line.rstrip()
        self.sequenceList.append(currentSequence)
        return self.sequenceIDList,self.sequenceList


def main():
    import sys
    rosalindReader = FileReader(sys.stdin)
    sequenceIDList,nucleotideSequence = rosalindReader.makeLists()
    createReadingFrames = OpenReadingFrames(nucleotideSequence)
    createReadingFrames.classController()

main()
