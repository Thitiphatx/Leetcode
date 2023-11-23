def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0

    start = 0
    n = len(s)

    # Skip leading whitespaces
    while start < n and s[start] == " ":
        start += 1

    # Check for empty string or all whitespaces
    if start == n:
        return 0

    # Initialize variables
    signMultiplier = 1
    result = 0

    # Handle sign
    if s[start] in ["-", "+"]:
        signMultiplier = -1 if s[start] == "-" else 1
        start += 1

    # Convert numeric characters to integer
    while start < n and s[start].isdigit():
        result = result * 10 + int(s[start])
        start += 1

    # Apply sign and check for overflow/underflow
    result *= signMultiplier
    if result < -2**31:
        return -2**31
    elif result > 2**31 - 1:
        return 2**31 - 1
    else:
        return result
    
print(myAtoi(" "))
