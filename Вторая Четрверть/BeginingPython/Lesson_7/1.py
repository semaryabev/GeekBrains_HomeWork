class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for n_list in self.matrix:
            for el in n_list:
                print(el,end=' ')
            print('')
        return 'Матрица выведена'

    def __add__(self,other):
        new_matrix = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(new_matrix)


m1 = Matrix([[3,3,1],[7,8,8]])
m2 = Matrix([[1,1,1],[1,1,1]])
print(m1)
print('')
print(m2)
print('')
print(m1 + m2)
