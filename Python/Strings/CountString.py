import re

def count_substring(string, sub_string):
    return len([m.start() for m in re.finditer('(?={})'.format(sub_string), string)])

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count