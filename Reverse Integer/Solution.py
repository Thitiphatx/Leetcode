def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    intString = str(x)
    if len(intString) == 1 :
        return x
    end = 0
    start = len(intString) - 1
    

    result = ""

    while(intString[start] == '0') :
        start -= 1

    if intString[0] == '-' :
        result += intString[0]
        end += 1
    
    for i in range(start, end-1, -1) :
        result += intString[i]
    
    if int(result) < pow(-2, 31) or int(result) > pow(2, 31) - 1:
        return 0
    else :
        return int(result)

print(reverse(1534236469))