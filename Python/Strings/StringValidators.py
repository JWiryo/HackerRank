if __name__ == '__main__':
    s = raw_input()
    isAlphaNum = isAlpha = isDigit = isLower = isUpper = False
    for char in list(s):
        if char.isalnum():
            isAlphaNum = True
        if char.isalpha():
            isAlpha = True
        if char.isdigit():
            isDigit = True
        if char.islower():
            isLower = True
        if char.isupper():
            isUpper = True

    print "{}\n{}\n{}\n{}\n{}".format(isAlphaNum, isAlpha, isDigit, isLower, isUpper)
