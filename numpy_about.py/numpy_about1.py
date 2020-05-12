import numpy
vector = numpy.array([5,10,15,20])
vector==10
#array[false,turn,false,false] type=bool
print(vector[0:3])
matrix=numpy.array(
        [1,2,3,4],
        [5,6,7,8],
        [11,22,33,44],)
print(matrix[:,2])
# 3 7 33
print(matrix[:,0:2])
"""
[1 2
5 6
11 22]"""
second_column =(matrix==22)
print(second_column)
print(matrix[second_lumn,:])
"""
11 22 33 44
"""
