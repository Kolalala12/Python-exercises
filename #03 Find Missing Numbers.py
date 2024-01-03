#03. find missing numbers
'''
Unlike the original exercise, I have rearranged the order with altered numbers. 
Thus, one additional step is added to sort in ascending order .
'''


def findMissingNumbers(nums):
    no_duplicates = sorted(set(nums))
    temp=[]
    
    for i in range (1, nums[-1]):
        if i not in no_duplicates:
            temp.append(i)
    return temp


#listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16] #original
listOfNumbers = [2, 1, 3, 5, 6, 7, 8, 10, 9, 11, 15, 14, 20]
print(findMissingNumbers(listOfNumbers))