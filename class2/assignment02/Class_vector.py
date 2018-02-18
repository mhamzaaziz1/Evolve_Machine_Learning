# simple vectors class
class vector:

    def __init__(self, x, m, n):
        self.x = x
        self.m = m
        self.n = n

    def is_SquareMatrix(self):
        if self.m == self.n:
            print("Matrix is square")
            return True
        else:
            print("Matrix is not square")
            return False

    def vector_transpose(self):
        result = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(0, self.m):
            for j in range(0, self.n):
                result[i][j] = self.x[j][i]

        return result

    def vector_product(self, x):
        result = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(len(self.x)):
           # iterate through columns of Y
            for j in range(len(x[0])):
               # iterate through rows of Y
               for k in range(len(x)):
                    result[i][j] += self.x[i][k] * x[k][j]
        return result

    def Identity_matrix(self):
        result = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.n):
                if i == j:
                    result[i][j] = 1
                else:
                    result[i][j] = 0
        return result

# orthogonal vector function
