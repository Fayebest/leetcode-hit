class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.back_track(board)
        print(board)

    def back_track(self,board):
        for row in range(0,9):
            for column in range(0,9):
                if board[row][column] == ".":
                    for i in range(1,10):
                        print("%d %s" %(i ,self.Isvalid(board,row,column,str(i))))
                        if self.Isvalid(board,row,column,str(i)):
                            board[row][column] = str(i)
                            if(self.back_track(board)):
                                return True
                            else:
                                board[row][column] = "."          
                    return False
                elif row == 8 and column == 8:
                    return True

    def Isvalid(self,board,row,column,target):
        for i in range(9):
            if board[row][i] == target or board[i][column] == target:
                return False
        for i in range(int(row/3)*3,int(row/3)*3+3):
            for j in range(int(column/3)*3,int(column/3)*3+3,):
                if board[i][j] == target:
                    return False
        return True

