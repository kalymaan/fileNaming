

def fileNaming(names):
    
    result = []
    dict ={}
    for i in range(len(names)):
        if names[i] not in dict.keys():
            result.append(names[i])
            dict[names[i]] = 0
            
        else:
            dict[names[i]] += 1
            newName = names[i] +'('+ str(dict[names[i]]) + ')'
            result.append(newName) 
            dict[newName] = 0
                           
    return result
test = ["doc", "doc", "image", "doc(1)", "doc"]

print fileNaming(test) 
#the output should be
#fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].