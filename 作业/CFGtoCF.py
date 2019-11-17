1class nVar:
    def __init__(self,Value =None,nextVar = None):
        self.Value = Value
        self.nextVar = []
        self.nextVar.append(nextVar)

class Node:
    def __init__(self,nVar = None,nextNode = None):
        self.Var = nVar
        self.nextNode = nextNode

class CFGtoCF:
    def __init__(self):
        self.Var = {}
        self.loadCFG()
        for i in self.Var:
            print(self.Var[i])

    def loadCFG(self):      #
        fo = open("CFG.txt",'r')
        CFGstring = fo.read()
        i = 0
        j = 0
        flag = 0
        while i < len(CFGstring):
            if CFGstring[i].isupper() and flag == 0:
                key = CFGstring[i]
                self.Var[key] = []
                flag = 1
                i = i+2
                j = i
            elif flag == 1 and (CFGstring[i] == '|' or CFGstring[i] == '\n' or i == len(CFGstring) -1):
                if i == len(CFGstring) -1:
                    self.Var[key].append(CFGstring[j:i+1])
                else:
                    self.Var[key].append(CFGstring[j:i])
                if CFGstring[i] == '\n':
                    flag = 0
                    i = i + 1
                else:
                    i += 1
                    j = i
            else:
                i += 1

        fo.close()

    def deleteE(self):          #删除空epison
        for key in self.Var:
            for i in self.Var[key]:
                if i == 'ξ':
                    self.subdelete(key)

    def subdelete(self,keyV):       #检测到有epison后从起始节点开始处理
        for key in self.Var:
            for i in self.Var[key]:
                if keyV in i:               #用全排列来处理一个产生式里面有多个空产生式的情况



    def combin(self,Var,keyV):
        for i in range(len(self.))



a = CFGtoCF()
