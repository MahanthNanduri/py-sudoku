import random
from tabulate import tabulate 
#A function to check whether the number is in the row
def Row(x, row, grid):
    if x in grid[row]:
        return True
    else:
        return False
#A function to check whether the number is in the column
def Col(x, col, grid):
    colList = []
    for i in range(9):
        colList.append(grid[i][col])
    if x in colList:
        return True
    else:
        return False
#above function checks whether number is in a 3*3 sqaure
def Square(x, row, col, grid):
    square = []
#This function will check which 3*3 square the number is located in the 9*9 grid
    if row < 3:
        if col < 3:
            square = [grid[i][0:3] for i in range(0, 3)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(0, 3)]
        else:
            square = [grid[i][6:9] for i in range(0, 3)]
#checks for the number in the first 3 rows and upto all 9 columns
    elif row < 6:
        if col < 3:
            square = [grid[i][0:3] for i in range(3, 6)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3, 6)]
        else:
            square = [grid[i][6:9] for i in range(3, 6)]
#checks from 3rd to 6th row and upto all 9 columns
    else:
        if col < 3:
            square = [grid[i][0:3] for i in range(6, 9)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(6, 9)]
        else:
            square = [grid[i][6:9] for i in range(6, 9)]
#finally it checks the last 3 rows and all acoloumns once again

    return bool(x in square[0]+square[1]+square[2])
#to check whether the 9*9 grid is filled
def isGridFilled(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                return False
    else:
        return True
#function to actually make the full sudoku table

def fillGrid(grid, tracker):

    values= [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for cellNo in range(81):
            row = cellNo // 9
            col = cellNo % 9

            random.shuffle(values)
            if grid[row][col] == 0:

                for testVal in values:
                    # 1. in the row
                    # 2. in the column
                    # 3. in the square

                    a = Row(testVal, row, grid)
                    b = Col(testVal, col, grid)
                    c = Square(testVal, row, col, grid)

                    if a == False and b == False and b == False:
                        #If testVal is unique in its row, column and (3*3) square
                        grid[row][col] = testVal

                        if isGridFilled(grid):
                            return True
                        else:
                            if fillGrid(grid, cellNo):
                               return True

                break 
    grid[row][col] = 0

grid = []
for i in range(9):
    #create empty grid
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

fillGrid(grid, 1)

#prints sudoku in the table
def Printgrid(Grid):
        print(tabulate(grid,tablefmt="fancy_grid"))

Printgrid(grid)
