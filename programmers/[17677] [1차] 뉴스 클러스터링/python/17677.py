from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    strArr1 = []
    strArr2 = []
    
    for i in range(len(str1)-1):
        if(str1[i].isalpha() and str1[i+1].isalpha()):
            strArr1.append(str1[i]+str1[i+1])
        
    for i in range(len(str2)-1):
        if(str2[i].isalpha() and str2[i+1].isalpha()):
            strArr2.append(str2[i]+str2[i+1])
            
    c1 = Counter(strArr1)
    c2 = Counter(strArr2)
    
    equalLength = len(list((c1 & c2).elements()))
    sumLength = len(list((c1 | c2).elements()))
    
    if (sumLength == 0 and equalLength == 0):
        return 65536
    else:
        return int(equalLength / sumLength * 65536)    