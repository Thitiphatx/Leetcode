def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    sList = list(s)
    pList = list(p)

    if len(sList) != len(pList) :
        return False

    #convert p
    p_length = len(p)
    for i in range(p_length) :
        if pList[i] == "*":
            sList[i] = "*"
        if pList[i] == ".":
            pList[i] = sList[i]
    s = "".join(sList)
    p = "".join(pList)
    
    return p == s

print(isMatch("ab", ".*"))