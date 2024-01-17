def solution(s):
    list_str = s.split(' ')

    result_str = ''
    for i in range(0, len(list_str)):
        
        list_char = list(list_str[i])
            
        for idx in range(0, len(list_char)):
            if(("a"<= list_char[0] <= "z")):
                list_char[0] = chr(ord(list_char[0])-32)
            elif(("A"<= list_char[idx] <= "Z") and idx!=0):
                list_char[idx] = chr(ord(list_char[idx])+32)
            
        result_str += ''.join(list_char)
        if(i == len(list_str)-1): break
        result_str += ' '
    
    return result_str

            