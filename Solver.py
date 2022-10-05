board = [
    [3,0,0,8,0,1,0,0,2],
    [2,0,1,0,3,0,6,0,4],
    [0,0,0,2,0,4,0,0,0],
    [8,0,9,0,0,0,1,0,6],
    [0,6,0,0,0,0,0,5,0],
    [7,0,2,0,0,0,4,0,9],
    [0,0,0,5,0,9,0,0,0],
    [9,0,4,0,8,0,7,0,5],
    [6,0,0,1,0,7,0,0,3]
]


def solve(b):
    found = find_zero(b)
    if not found:
        return True
    else:
        row, col = found    
    for i in range(1,10):
        if correct(b,i,(row,col)):
            b[row][col] = i
            if solve(b):
                return True
            b[row][col] = 0 
    return False


def correct(b,num,pos):
    # check row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i :
            return False
    # check column
    for i in range(len(b[0])):
        if b[i][pos[1]] == num and pos[0] != i :
            return False        
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
   
    for i in range(box_y*3,box_y*3 +3):
        for j in range(box_x*3,box_x*3 +3):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True
 

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(b[0]))  :
            if j % 3 == 0 and j != 0 :
                print(" | ", end="")  

            if j == 8 :
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")        

def find_zero(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j) #row, col
    return None  


print_board(board)
solve(board)
print("______________________________")
print_board(board)