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
if v.vector_product(v.Identity_matrix()) ==matrix:
    print(matrix,"is identity matrix")
else:
    print(matrix, "is not identity matrix")
