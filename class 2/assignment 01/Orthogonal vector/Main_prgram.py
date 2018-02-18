from Class_vector import vector

m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = [];
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(0, m):
    for j in range(0, n):
        print ("entry in row[", i + 1, "] column[ ", j + 1, "]")
        matrix[i][j] = input('Enter value for matrix=  ')
print("end of matrix input")
v = vector(matrix, m, n)
print ("result: ",v.vector_product(v.Identity_matrix()))




if v.is_SquareMatrix():
    if v.vector_product(v.vector_transpose()) == v.Identity_matrix():
        print("Matrix is orthogonal")
    else:
        print("Matrix is not orthogonal")
else:
    print("not a square Matrix not an Orthogonal")
