def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    
    start = 0
    end = 0

    def runner(left, right) :
        while (left >= 0 and right < len(s) and s[left] == s[right]) :
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)) :
        left1, right1 = runner(i, i)
        left2, right2 = runner(i, i+1)

        if right1 - left1 > end - start :
            start, end = left1, right1
            
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end+1]



print(longestPalindrome("aaaa"))



