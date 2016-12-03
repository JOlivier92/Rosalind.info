#!/usr/bin/env python3
# Name: Joseph Olivier

class ConsensusChecker:
    def __init__(self,sequenceIDList,sequenceList):
        import numpy as np
        self.sequenceIDList = sequenceIDList
        self.sequenceList = sequenceList
        #initializes numpy array with 4 rows and columns == length of a sequence.
        self.countArray = np.zeros([4,len(self.sequenceList[0])])
        
    def mainController(self):
        #Run through each sequence, create counter array
        for i in range(0,len(self.sequenceIDList)):
            self.addtoCounterArray(self.sequenceList[i])
        #After counter array has been created, print the output.
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
        #Look down each column of the counter array
        #Find max, locate it, and add to outputSequence accordingly. 
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
        print(outputSequence)\
        #Just pushing np Array to list for easier printing...
        listofArray = self.countArray.tolist()
        #outer loop > each row
        #inner loop > each column (each cell within the row)
        for i in range(0,len(listofArray)):
            if i == 0:
                print("A: ",end="")
            elif i == 1:
                print("C: ",end="")
            elif i == 2:
                print("G: ",end="")
            elif i == 3:
                print("T: ",end="")
            for item in listofArray[i]:
                print(int(item),end=" ")
            print("")
        sys.exit()





class FileReader:
    def __init__(self,filetoRead):
        self.filetoRead = filetoRead
        self.sequenceIDList = list()
        self.sequenceList = list()

    def reader(self):
        self.currentSequence = str()
        for line in self.filetoRead:
            if line.startswith(">"):
                #prevents empty sequence being added before first sequenceID is added.
                if self.sequenceIDList:
                    self.sequenceList.append(self.currentSequence)
                self.sequenceIDList.append(line.rstrip())
                self.currentSequence = str()
            else:
                self.currentSequence+=line.rstrip().upper()
        #Add last sequence to sequenceList
        self.sequenceList.append(self.currentSequence)
        return self.sequenceIDList,self.sequenceList

def main():
    import sys
    fastain = FileReader(sys.stdin)
    sequenceIDList,sequenceList = fastain.reader()
    output = ConsensusChecker(sequenceIDList,sequenceList)
    print(output.mainController())

main()