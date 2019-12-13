class nVar:
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
        # for i in self.Var:
        #     print(self.Var[i])
        self.deleteE()
        # for i in self.Var:
        #     print(self.Var[i])
        self.removeUnit()
        # for i in self.Var:
        #      print(self.Var[i])
        self.introVar()
        for i in self.Var:
            print(i+"->",end="")
            for j in range(len(self.Var[i])):
                print(self.Var[i][j],end="")
                if j != len(self.Var[i])-1:
                    print("|",end="")
            print()


    def loadCFG(self):      #
        fo = open("CFG.txt",'r')
        CFGstring = fo.read()
        i = 0
        j = 0
        flag = 0
        self.Var["Z"] = []          #开始节点 先设置来占位
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
        self.Var["Z"].append(list(self.Var.keys())[1])
        fo.close()

    def deleteE(self):          #删除空epison
        self.hasdel = []        #维护一个集合，里面装的是已经删除过的空产生事，防止重复产生空产生式
        self.flag = 1                #flag = 1 表示有新的空产生式产生，需要重新遍历一次CFG
        while(self.flag == 1):
            self.flag = 0
            for key in self.Var:
                for i in self.Var[key]:
                    if i == 'ξ':
                        self.hasdel.append(key)
                        self.Var[key].remove('ξ')       #先移除空产生式
                        if len(self.Var[key]) == 0:
                            del dict[key]
                        self.subdelete(key)

    def subdelete(self,keyV):       #检测到有epison后从起始节点开始处理
        for key in self.Var:
            for i in self.Var[key]:
                if keyV in i:            #用全排列来处理一个产生式里面有多个空产生式的情况
                    mapdict = {}
                    count = 0
                    for j in range(len(i)):
                        if i[j] == keyV:
                            mapdict[count] = j
                            count += 1
                    self.combination = []
                    self.combin(len(mapdict.keys()),0,[])
                    self.combination.remove([])
                    for tindexs in self.combination:
                        tempexp = i
                        for tindex in range(len(tindexs)-1,-1,-1):
                            tempexp = tempexp[:mapdict[tindexs[tindex]]] + tempexp[mapdict[tindexs[tindex]]+1:]
                        if len(tempexp) == 0 and key not in self.hasdel:
                            self.Var[key].append('ξ')
                            self.flag = 1
                        elif tempexp not in self.Var[key]:
                            self.Var[key].append(tempexp)

    def combin(self,nums,sta,path):
        self.combination.append(path[:])
        for i in range(sta,nums):
            path.append(i)
            self.combin(nums,i+1,path)
            path.pop()

    def removeUnit(self):           #移除单元产生式
        for keys in self.Var:           #先移除S->S
            for exp in self.Var[keys]:
                if exp == keys:
                    self.Var[keys].remove(exp)

        for keys in self.Var:
            deltemp = []
            addtemp = []
            for exp in self.Var[keys]:
                if len(exp) == 1 and exp.isupper():
                    deltemp.append(exp)
                    for i in self.Var[exp]:
                        addtemp.append(i)
            for i in deltemp:
                self.Var[keys].remove(i)
            for i in addtemp:
                self.Var[keys].append(i)

    def introVar(self):             #引入新的变量来解决ABCD...这种产生式
        Termin = []
        tempterdict = {}               #创建一个临时字典 方便通过终结符寻找key
        tempvardict = {}
        varcount = 0
        tercount = 0

        for key in list(self.Var.keys()):  # 找出长度大于2的产生式 用新变量替代
            for exp in range(len(self.Var[key])):
                if len(self.Var[key][exp]) > 2:
                    tempstring = self.Var[key][exp]
                    for num in range(1,len(tempstring) - 1):
                       if tempstring[num:] not in tempvardict.keys():
                            newvar = "#V" + str(varcount) + "#"
                            varcount += 1
                            tempvar = "#V" + str(varcount) + "#"
                            self.Var[newvar] = []
                            if num == len(tempstring) - 2:
                                self.Var[newvar].append(str(tempstring[num:]))
                            else:
                                self.Var[newvar].append(str(tempstring[num])+tempvar)
                            tempvardict[tempstring[num:]] = newvar
                            if num == 1:
                                self.Var[key][exp] = tempstring[num-1] + tempvardict[tempstring[num:]]
                       else:
                            if num == 1:
                                self.Var[key][exp] = tempstring[num-1] + tempvardict[tempstring[num:]]
                            else:
                                self.Var[key][exp] = tempstring[num - 1] + tempvardict[tempstring[num:]]
                            break



        for key in list(self.Var):                                #替换终结符
            for exp in range(len(self.Var[key])) :
                for alpha in self.Var[key][exp]:
                    if alpha.islower() and len(self.Var[key][exp]) > 1:
                        if alpha not in tempterdict.keys():
                            keys = "#T" + str(tercount) + "#"
                            tercount += 1
                            self.Var[keys] = []
                            self.Var[keys].append(alpha)
                            tempterdict[alpha] = keys
                        self.Var[key][exp] = self.Var[key][exp].replace(alpha,tempterdict[alpha],1)




a = CFGtoCF()