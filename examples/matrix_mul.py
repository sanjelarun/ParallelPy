import random


def matInput(mat, rows, cols):
    for row in range(rows):
        for col in range(cols):
            mat[row][col] = int(input("Enter element? "))
    return mat


## Matrix 1 dimension
row_mat1 = int(input("Enter no of rows in the first matrix:"))
col_mat1 = int(input("Enter no of columns in the first matrix:"))

## Creates a random matrix of given dimensions for intialization
mat1 = [[random.random() for col in range(col_mat1)] for row in range(row_mat1)]
mat1 = matInput(mat1, row_mat1, col_mat1)

## Matrix 2 dimension
row_mat2 = int(input("Enter no of rows in the second matrix:"))
col_mat2 = int(input("Enter no of columns in the second matrix:"))

## Creates a random matrix of given dimensions for intialization
mat2 = [[random.random() for col in range(col_mat2)] for row in range(row_mat2)]
mat2 = matInput(mat2, row_mat2, col_mat2)

## Output matrix intialization
out_mat = [[random.random() for col in range(col_mat2)] for row in range(row_mat1)]

if col_mat1 == row_mat2:
    i: int = 0
    while i < row_mat1:
        j: int = 0
        while j < col_mat2:
            out_mat[i][j] = 0
            k = 0
            while k < col_mat1:
                out_mat[i][j] += mat1[i][k] * mat2[k][j]
                k += 1
            print(out_mat[i][j], end='\t')
            j += 1
        i += 1
        print()
    ##print(out_mat)
else:
    print("Invalid Dimensions")
