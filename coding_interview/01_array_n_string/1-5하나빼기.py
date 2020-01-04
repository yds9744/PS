def solution(str1, str2):
    if str1==str2: return True

    flag = False

    if len(str1) == len(str2):
        for i, j in zip(str1, str2):
            if i!=j:
               if flag: return False
               else: flag = True
        return True

    elif len(str1) < len(str2):
        str1, str2 = str2, str1
        
    if len(str1) == len(str2) + 1 :
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                if flag: return False
                else:
                    flag = True
                    str2 = str2[:i] + str1[i] + str2[i:]
        return True
    
    return False
