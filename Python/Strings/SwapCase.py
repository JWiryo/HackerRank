def swap_case(s):
    new_string = ""
    for character in s:
        if character.islower():
            new_string += character.upper()
        else:
            new_string += character.lower()
    return new_string


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
