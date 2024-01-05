#04. Group Elements of Same Indices

import numpy as np

#method 1
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
transpose = np.transpose(inputLists)
print(transpose, '\n')
'''
output:
[[10 40 70]
 [20 50 80]
 [30 60 90]] 
'''

output = " ".join(map(str, transpose))
print(output, '\n')
'''
output:
[10 40 70] [20 50 80] [30 60 90] 
'''

#method 2
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
output = []
index = 0

for i in range(len(inputLists)):
    output.append([])
    for j in range(len(inputLists)):
        output[index].append(inputLists[j][index])
        #print(output)
    index+=1
    
print(output[0], output[1], output[2])
'''
output:
[10, 40, 70] [20, 50, 80] [30, 60, 90]
'''

#method 3
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for j in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
'''Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]'''
