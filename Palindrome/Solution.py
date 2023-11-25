def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    intStr = str(x)
    n = len(intStr)
    start = 0
    end = n - 1
    isPal = True

    while (start < end) :
        if intStr[start] != intStr[end] :
            isPal = False
            break
        else :
            start += 1
            end -= 1
    return isPal


# faster
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string = str(x)
    return string == string[::-1]