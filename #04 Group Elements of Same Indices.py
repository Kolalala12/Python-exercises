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