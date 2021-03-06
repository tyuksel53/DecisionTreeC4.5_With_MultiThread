from threading import Thread
from time import sleep
import math
from Node import BinaryTree
class Django:
    exitFlag = 0
    generalEntropy=0    ## general_entropy
    global columnSize   ## how many columns in file
    filePath = ""       ## file path
    fileRow = 0         ## file row counter
    ColumnEntropys = []
    ColumnInfomationGain = []
    node_conter = 0
    root = None
    def __init__(self,path): ## class constructor
        try:
            self.filePath = path ## adding file path
            self.GetFuncsize()   ## adding columnsize
            self.generalEntropy = self.findGeneralEntropy() ## finding general entropy
        except Exception as ex:
            print ex
            raw_input()

    def GetFuncsize(self):
        try:
            file = open(self.filePath, "r")
            line = file.readline()
            line = line.split(',')
            self.columnSize = len(line) ## Initialize data columnsize
        except Exception as ex:
            print ex
            raw_input()

    def EntropyFormula(self,total,current): ## EntropyFormula definition
        dummy = current/ float(total)
        dummy = dummy * math.log(dummy, 2)
        return dummy * -1
    
    def CompareZ(self,columnNum,columnValue,current):
        try:
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            i=0
            RowCount = 0
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  if line[columnNum] == columnValue: ## find specific Area
                      for i  in range(len(VariableInResult)): ## check variable is already added
                          if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                             VariableInResultCounter[i] +=1 ## count up 
                             Control = 1 ## variable is finded
                      if Control == 0: ## if variable is not finded then add variable
                         VariableInResult.append(line[len(line)-1])
                         VariableInResultCounter.append(1)
                      Control = 0
                      RowCount += 1
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(RowCount,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    def findAllEntropy(self): ## finding all column's entropyes
        try:
            for i in range(self.columnSize-1):
                self.findEntropy(self.columnSize - i,self.root)

            for i in range(len(self.ColumnEntropys)):
                natay = self.generalEntropy -  self.ColumnEntropys[i]
                self.ColumnInfomationGain.append(natay)
                
            for i in range(len(self.ColumnInfomationGain)):
                if self.ColumnInfomationGain[i] ==  max(self.ColumnInfomationGain):
                    print i,"  ",max(self.ColumnInfomationGain)
                    break
            control = 5
            self.root.f = i
            self.findChild(self.root,i)
            self.printTree(self.root)
            control = self.nodeCheck(self.root)
            if control == 0:
               print "bitti"
            self.splitNode(self.root)
            self.printTree(self.root)
            thread1 = Thread(target = self.DecisionL, args = (self.root.getLeftChild(), ))
            thread2 = Thread(target = self.DecisionR, args = (self.root.getRightChild(), ))
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            #thread.start_new_thread( self.DecisionR,( self.root.getRightChild(),) )
            #thread.start_new_thread( self.DecisionL, self.root.getLeftChild() )
        
        except Exception as ex:
            print ex
            raw_input()

    def DecisionL(self,current,delay, counter):
            print current.rootid ,"-" ,current.f ,"-",current.split
            self.ColumnEntropys = None
            self.ColumnEntropys = []
            self.ColumnInfomationGain = None
            self.ColumnInfomationGain = []

            for i in range(self.columnSize-1):
                self.findEntropy(self.columnSize - i,current)

            for i in range(len(self.ColumnEntropys)):
                natay = self.generalEntropy -  self.ColumnEntropys[i]
                self.ColumnInfomationGain.append(natay)
                
            for i in range(len(self.ColumnInfomationGain)):
                if self.ColumnInfomationGain[i] ==  max(self.ColumnInfomationGain):
                    print i,"  ",max(self.ColumnInfomationGain)
                    break

            current.setNodef(i)
            self.findChild(current,i)
            self.printTree(self.root)
            self.splitNode(current)
            
            control = self.nodeCheck(current.getLeftChild())
            if control == 0:
               print "bitti"
               return
            
            self.DecisionL(current.getLeftChild())
            self.DecisionR(current.getRightChild())
    def DecisionR(self,current,delay, counter):
            print current.rootid ,"-" ,current.f ,"-",current.split
            self.ColumnEntropys = None
            self.ColumnEntropys = []
            self.ColumnInfomationGain = None
            self.ColumnInfomationGain = []

            for i in range(self.columnSize-1):
                self.findEntropy(self.columnSize - i,current)

            for i in range(len(self.ColumnEntropys)):
                natay = self.generalEntropy -  self.ColumnEntropys[i]
                self.ColumnInfomationGain.append(natay)
                
            for i in range(len(self.ColumnInfomationGain)):
                if self.ColumnInfomationGain[i] ==  max(self.ColumnInfomationGain):
                    print i,"  ",max(self.ColumnInfomationGain)
                    break

            current.setNodef(i)
            self.findChild(current,i)
            self.printTree(self.root)
            self.splitNode(current)
            
            control = self.nodeCheck(current.getRightChild())
            if control == 0:
               print "bitti"
               return
            sleep(1)
            self.DecisionL(current.getLeftChild())
            self.DecisionR(current.getRightChild())
           
    def nodeCheck(self,current):
        try:
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  for i  in range(len(VariableInResult)): ## check variable is already added
                      if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                         VariableInResultCounter[i] +=1 ## count up 
                         Control = 1 ## variable is finded
                  if Control == 0: ## if variable is not finded then add variable
                     VariableInResult.append(line[len(line)-1])
                     VariableInResultCounter.append(1)
                  Control = 0
                  Count += 1 ## file row counter
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(Count,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    def splitNode(self,current):
        try:
            current.insertRight(self.node_conter)
            self.node_conter +=1
            current.insertLeft(self.node_conter)
            self.node_conter +=1
            print current.f ,"-",current.split
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  if float(line[current.f]) < float(current.split):
                     line = [s.replace('\n', '') for s in line]
                     #print line
                     current.getLeftChild().setNodeLines(line)
                  if float(line[current.f]) >= float(current.split):
                     line = [s.replace('\n', '') for s in line]
                     current.getRightChild().setNodeLines(line)
        except Exception as ex:
            print ex
            raw_input()
    def findChild(self,current,funcNumber):
        split = []
        if current.f == 0:
            split.append(50)
            split.append(60)
            split.append(70)
        if current.f == 1:
            split.append(62)
            split.append(63)
            split.append(64)
        if current.f == 2:
            split.append(5)
            split.append(10)
            split.append(19)
        childEntropy = []
        dummy = 0
        dummy_2 = 0
        for i in range(len(split)):
            asd = float(len(current.Lines))
            kd = float(asd/self.fileRow)
            dummy =  asd * self.findEntropyBySplit(funcNumber,split[i],funcNumber,0,current)
            dummy_2 = asd * self.findEntropyBySplit(funcNumber,split[i],funcNumber,1,current)
            toplam = dummy+dummy_2
            print split[i],"  -  ", dummy , "  -  " , dummy_2 , "  -  " ,toplam
            childEntropy.append(toplam)

        for i in range(len(childEntropy)):
                if childEntropy[i] ==  max(childEntropy):
                    print split[i],"  ",max(childEntropy)
                    current.setNodeSplit(split[i])
    def findEntropyBySplit(self,ColumnNum,split,funcNumber,control,current):
         try:
            VariableInResult = []
            VariableInResultCounter = []
            VariableInZColumn = []
            VariableInZColumnCounter = []
            Count = 0
            Control = 0
            i,t,m =0,0,0
            count = 0
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  line = [s.replace('\n', '') for s in line]
                  if control == 1:
                     if float(line[current.f]) >= float(split):
                          for i  in range(len(VariableInResult)):
                              if VariableInResult[i] == line[len(line)-current.f -1]:
                                 VariableInResultCounter[i] +=1
                                 Control = 1
                          if Control == 0:
                             VariableInResult.append(line[len(line)-current.f -1])
                             VariableInResultCounter.append(1)
                  else:
                     if float(line[current.f]) < float(split):
                           
                          for i  in range(len(VariableInResult)):
                              if VariableInResult[i] == line[len(line)-current.f -1]:
                                 VariableInResultCounter[i] +=1
                                 Control = 1
                          if Control == 0:
                             VariableInResult.append(line[len(line)-current.f -1])
                             VariableInResultCounter.append(1)
                  Control = 0
            TotalEntropy = 0
            for i  in range(len(VariableInResult)):
                a = ( VariableInResultCounter[i] / float(self.fileRow) )
                b = self.CompareZbySplit(self.columnSize-current.f,VariableInResult[i],split,current.f,control,current)
                dummy = a * b
                TotalEntropy = dummy + TotalEntropy
                ##print VariableInResult[i]," ",  VariableInResultCounter[i], " ",dummy
            return TotalEntropy
         except Exception as ex:
            print ex
            raw_input()
    def CompareZbySplit(self,columnNum,columnValue,split,funcNumber,control,current):
        try:
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            i=0
            RowCount = 0
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  if control == 1:
                      if float(line[current.f]) >= float(split):
                              for i  in range(len(VariableInResult)): ## check variable is already added
                                  if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                                     VariableInResultCounter[i] +=1 ## count up 
                                     Control = 1 ## variable is finded
                              if Control == 0: ## if variable is not finded then add variable
                                 VariableInResult.append(line[len(line)-1])
                                 VariableInResultCounter.append(1)
                              Control = 0
                              RowCount += 1
                  else:
                       if float(line[current.f]) < float(split):
                              for i  in range(len(VariableInResult)): ## check variable is already added
                                  if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                                     VariableInResultCounter[i] +=1 ## count up 
                                     Control = 1 ## variable is finded
                              if Control == 0: ## if variable is not finded then add variable
                                 VariableInResult.append(line[len(line)-1])
                                 VariableInResultCounter.append(1)
                              Control = 0
                              RowCount += 1
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(RowCount,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    def findEntropy(self,ColumnNum,current): ## finding entropy column by column
        try:
            VariableInResult = []
            VariableInResultCounter = []
            VariableInZColumn = []
            VariableInZColumnCounter = []
            Count = 0
            Control = 0
            i,t,m =0,0,0
            for i in range(len(current.Lines)):
                  line = current.Lines[i]
                  line = [s.replace('\n', '') for s in line]
                  for i  in range(len(VariableInResult)):
                      if VariableInResult[i] == line[len(line)-ColumnNum]:
                         VariableInResultCounter[i] +=1
                         Control = 1
                  if Control == 0:
                     VariableInResult.append(line[len(line)-ColumnNum ])
                     VariableInResultCounter.append(1)
                  Control = 0
            TotalEntropy = 0
            for i  in range(len(VariableInResult)):
                a = ( VariableInResultCounter[i] / float(self.fileRow) );
                b = self.CompareZ(self.columnSize-ColumnNum,VariableInResult[i],current)
                dummy = a *b
                TotalEntropy = dummy + TotalEntropy
            self.ColumnEntropys.append(TotalEntropy)
        except Exception as ex:
            print ex
            raw_input()
    def findGeneralEntropy(self): ## finding general entropy
        try:
            file = open(self.filePath, "r")
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            i=0
            self.root = BinaryTree(self.node_conter)
            self.node_conter += 1
            while True:
                  line = file.readline()
                  if line == '': ## if it's at the end of file
                     break
                  line = line.split(',')
                  self.root.Lines.append(line)
                  for i  in range(len(VariableInResult)): ## check variable is already added
                      if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                         VariableInResultCounter[i] +=1 ## count up 
                         Control = 1 ## variable is finded
                  if Control == 0: ## if variable is not finded then add variable
                     VariableInResult.append(line[len(line)-1])
                     VariableInResultCounter.append(1)
                  Control = 0
                  self.fileRow += 1 ## file row counter
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(self.fileRow,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    
    
    def printTree(self,tree):
       try:    
        if tree != None:
                self.printTree(tree.getLeftChild())
                print(tree.getNodeValue())
                self.printTree(tree.getRightChild())
       except Exception as ex:
            print ex
            raw_input()
