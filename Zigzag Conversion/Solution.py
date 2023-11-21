def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    rows = [''] * numRows
    index = 0
    step = 1

    for char in s:
        rows[index] += char

        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1

        index += step
    result = ''.join(rows)
    return result

convert("AB", 1)