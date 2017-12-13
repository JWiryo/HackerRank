import re

def count_substring(string, sub_string):
    count = 0
    for msg in xrange(len(string)):
        if msg == string.find(sub_string):
            count += 1
    return  count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count