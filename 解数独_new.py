import copy
class Cell:
    def __init__(self):
        self.value = 0
        self.constrain = [0 for i in range(10)]     # =1 不能为该值
        self.possibilenum = 9


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        print("----->")
        self.cells = [[Cell() for i in range(9)] for j in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.' and not self.setcells(i,j,int(board[i][j]) ) :
                    print("error",end='')
                    return
    
       
        if not self.findEmptycell():
            print("error",end='')
            return
        print("---->temp%s" %(self.cells[8][8].value))
        
        for i in range(0,9):
            for j in range(0,9):
                board[i][j] = str(self.cells[i][j].value)
        
        for i in range(0,9):
            print(board[i])



    def setcells(self,x,y,value):
        if self.cells[x][y].value == value:
            return True
        if self.cells[x][y].constrain[value] == 1:
            print("----->  1")
            return False
        self.cells[x][y].value = value
        self.cells[x][y].constrain = [1] *10
        self.cells[x][y].constrain[value] = 0
        self.cells[x][y].possiblenum = 1
        for i in range(0,9):
            if (i != y and not self.toConstrain(x,i,value)) or (i !=x and not self.toConstrain(i,y,value)):
                print("----->  2")
                return False
    
        for i in range(x//3*3,x//3*3+3):
            for j in range(y//3*3,y//3*3+3):
                if (i != x or j != y) and not self.toConstrain(i,j,value):
                    print("----->  3")
                    return False    
        return True    

        

    def toConstrain(self,x,y,value):  #传递constrain possible=1就尽早填入可以填的数减少回溯
        if self.cells[x][y].constrain[value]:
            return True
        if self.cells[x][y].value == value:
            print("----->  4")
            return False
        self.cells[x][y].constrain[value] = 1
        self.cells[x][y].possibilenum -= 1
        if self.cells[x][y].possibilenum > 1:
            return True
        if self.cells[x][y].possibilenum == 1:
            for i in range(1,10):
                if self.cells[x][y].constrain[i] == 0:
                    return self.setcells(x,y,i)
        return False

    def mysort(self,bt):      #按照能填入数字的多少从小到大排序
        for i in range(len(bt)):
            for j in range(len(bt)-1):
                if self.cells[bt[j][0]][bt[j][1]].possibilenum > self.cells[bt[j+1][0]][bt[j+1][1]].possibilenum:
                    bt[j] ,bt[j+1] = bt[j+1] ,bt[j]
             
                    
    def findEmptycell(self):
        bt = []
        for i in range(0,9):
            for j in range(0,9):
                if self.cells[i][j].value == 0:
                    bt.append([i,j])
        self.mysort(bt)
        print()
        for i in range(len(bt)):
            print("%d  " %(self.cells[bt[i][0]][bt[i][1]].possibilenum),end='')
            print(bt[i])
        return self.back_track(0,bt)
    
    def back_track(self,k,bt):
        if k >= len(bt):
            return True
        x = bt[k][0]
        y = bt[k][1]
        print("%d<--->%d"%(x,y))
        if x == 2 and y == 0:
            print("aaa")
        if self.cells[x][y].value:
            return self.back_track(k+1,bt)
        
        tempconstrain = copy.deepcopy(self.cells[x][y].constrain)
        temp = copy.deepcopy(self.cells)
        for v in range(1,10):
            if not tempconstrain[v]:
                if self.setcells(x,y,v):
                    if self.back_track(k+1,bt):
                        return True
                self.cells = temp
        return False



a = Solution()
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
a.solveSudoku(board)