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
        cells = [[Cell() for i in range(9)] for j in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.' and not self.setcells(i,j,cells,int(board[i][j]) ) :
                    print("error",end='')
                    print([i,j])
                    for ix in range(0,9):
                        for jy in range(0,9):
                            print(cells[ix][jy].constrain)
                    print(cells[i][j].constrain)
                    return
                elif board[i][j] != '.':
                        print([i,j],end='')
                        print(cells[i][j].value)
        
        print("----->")
        if not self.findEmptycell(cells):
            return
        print("----->")
        for i in range(0,9):
            for j in range(0,9):
                board[i][j] = str(cells[i][j].value)
        
        #print(board)



    def setcells(self,x,y,cells,value):
        if cells[x][y].value == value:
            return True
        if cells[x][y].possibilenum == 1:
            return False
        cells[x][y].value = value
        cells[x][y].constrain = [1] *10
        cells[x][y].constrain[value] = 0
        cells[x][y].possiblenum = 1
        for i in range(0,9):
            if (i != y and not self.toConstrain(x,i,cells,value)) or (i !=x and not self.toConstrain(i,y,cells,value)):
                return False
        for i in range(x//3*3,x//3*3+3):
            for j in range(y//3*3,y//3*3+3):
                if (i != x and j!=y) and not self.toConstrain(i,j,cells,value):
                    return False
        return True

    def toConstrain(self,x,y,cells,value):  #传递constrain possible=1就尽早填入可以填的数减少回溯
        if cells[x][y].constrain[value]:
            return True
        if cells[x][y].value == value:
            return False
        cells[x][y].constrain[value] = 1
        cells[x][y].possibilenum -= 1
        if cells[x][y].possibilenum == 1:
            for i in range(1,10):
                if cells[x][y].constrain[i] == 0:
                    return self.setcells(x,y,cells,i)
        else:
            return True

    def mysort(self,cells,bt):      #按照能填入数字的多少从小到大排序
        temp = []
        for i in range(len(bt)):
            for j in range(len(bt)-1):
                if cells[bt[j][0]][bt[j][1]].possibilenum > cells[bt[j+1][0]][bt[j+1][1]].possibilenum:
                    bt[j] ,bt[j+1] = bt[j+1] ,bt[j]
             
                    
    def findEmptycell(self,cells):
        bt = []
        for i in range(0,9):
            for j in range(0,9):
                if cells[i][j].value == 0:
                    bt.append([i,j])
        self.mysort(cells,bt)
        return self.back_track(0,bt,cells)
    
    def back_track(self,k,bt,cells):
        if k >= bt.size():
            return True
        x = bt[k][0]
        y = bt[k][1]
        if cells[x][y].value:
            return self.back_track(k+1,bt,cells)
        
        temp = cells
        for v in range(1,10):
            if not cells[x][y].constrain[v]:
                if self.setcells(x,y,cells,v):
                    if self.back_track(k+1,bt,cells):
                        return True
            cells = temp
        return False



a = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a.solveSudoku(board)