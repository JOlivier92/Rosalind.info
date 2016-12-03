#!/usr/bin/env python3
# Name: Joseph Olivier

class ConsensusChecker:
    def __init__(self,sequenceIDList,sequenceList):
        import numpy as np
        self.sequenceIDList = sequenceIDList
        self.sequenceList = sequenceList
        self.countArray = np.zeros([4,len(self.sequenceList[0])])
        
    def mainController(self):
        for i in range(0,len(self.sequenceIDList)):
            self.addtoCounterArray(self.sequenceList[i])
        self.outputPrinter()

    def addtoCounterArray(self,sequence):
        import numpy as np
        import sys
        for i in range(0,len(sequence)):
            if sequence[i] == "A":
                self.countArray[0][i] += 1
            elif sequence[i] == "C":
                self.countArray[1][i] += 1
            elif sequence[i] == "G":
                self.countArray[2][i] += 1
            elif sequence[i] =="T":
                self.countArray[3][i] += 1
            else:
                sys.stderr.write("invalid character in one of the sequences...")
                sys.exit()
    def outputPrinter(self):
        import sys
        import numpy as np
        outputSequence = str()
        for i in range(0,len(self.countArray[0])):
            column = self.countArray[:,i].tolist()
            columnMax = max(column)
            nucleotideIndex = column.index(columnMax)
            if nucleotideIndex == 0:
                outputSequence+="A"
            elif nucleotideIndex == 1:
                outputSequence+="C"
            elif nucleotideIndex == 2:
                outputSequence+="G"
            else:
                outputSequence+="T"
        print(outputSequence)
        poop = self.countArray.tolist()
        for i in range(0,len(poop)):
            if i == 0:
                print("A: ",end="")
            elif i == 1:
                print("C: ",end="")
            elif i == 2:
                print("G: ",end="")
            elif i == 3:
                print("T: ",end="")
            for item in poop[i]:
                print(int(item),end=" ")
            print("")


        # print("A: "+ str(self.countArray[0]))
        # print("C: "+ str(self.countArray[1]))
        # print("G: "+ str(self.countArray[2]))
        # print("T: "+ str(self.countArray[3]))


        sys.exit()





class FileReader:
    """
    This is the fileReader in the program. Its function is two create two objects:
    One xseq object which will contain a list with the name of the xsequence as well as
    the sequence itself. The second object will be a dictionary with all of the ySequence
    names paired with their sequences.
    """
    def __init__(self,filetoRead):
        """
        The only input object for this class is the fasta file which needs to be read.
        xSequence will be a list to contain the sequenceID as well as the sequence of
        the first sequence in the fasta file. The ySequenceList will contain all of the 
        subsequent sequenceIDs with their sequences.
        """
        self.filetoRead = filetoRead
        self.sequenceIDList = list()
        self.sequenceList = list()

    def reader(self):
        """
        This is the function that actually does the parsing of the fasta file. It looks
        at every line in the file and determines whether it is the start of a new sequence.
        If it is the first sequence in the file, it adds the sequenceID and the sequence to the
        xSequence object. Else, it will add the sequenceID and the sequence to the ySequenceList
        object.
        This function will return the xSequence object (list) and the ySequenceList object (list)
        """
        self.currentSequence = str()
        for line in self.filetoRead:
            #Check to see if it's a titleline
            if line.startswith(">"):
                if self.currentSequence:
                    self.sequenceList.append(self.currentSequence)
                self.sequenceIDList.append(line.rstrip())
                self.currentSequence = str()
            else:
                self.currentSequence+=line.rstrip().upper()
        self.sequenceList.append(self.currentSequence)
        return self.sequenceIDList,self.sequenceList

def main():
    import sys
    fastain = FileReader(sys.stdin)
    sequenceIDList,sequenceList = fastain.reader()
    output = ConsensusChecker(sequenceIDList,sequenceList)
    print(output.mainController())

main()