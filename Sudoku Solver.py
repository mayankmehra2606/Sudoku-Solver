def findEmpty(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def used_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


def used_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def used_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


def checkLocation(arr, row, col, num):
    return not used_row(arr, row, num) and not used_col(arr, col, num) and not used_box(arr, row - row % 3, col - col % 3, num)


def solveSudoku(board):
    l = [0, 0]
    if not findEmpty(board, l):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if checkLocation(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board):
                return True
            board[row][col] = 0
    return False


board = [[int(ele) for ele in input().split()]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
