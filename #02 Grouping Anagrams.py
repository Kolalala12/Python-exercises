#02 Grouping Anagrams
'''
The existing joint word will be printed for checking the key exists in the temp dict. 
In case to ensure my work is correct, the updated temp{} will be printed also for self checking.
If aim to show the final result, the additional "print" can be #
'''
def group_anagrams(words):
    temp = {}
    for i in range(len(words)):
        #to rearrange the letters for each word in list
        joint = "".join(sorted(words[i])) 
        print('Current rearranged word:',joint) #can be omit

        #check if the word in dict
        if joint not in temp:
            #create a new key:values
            temp[joint] = [words[i]]
            print(temp, '\n') #can be omit
        else:
            #append the existing values
            temp[joint].append(words[i])
            print(temp, '\n') #can be omit
    return temp.values() 
    
words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
