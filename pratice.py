def palandrom_check(str1):
    rev_str = str1[::-1]
    if rev_str == str1:
        return True
    else:
        False
str1 = "malayalam"
result = palandrom_check(str1)
print(result)