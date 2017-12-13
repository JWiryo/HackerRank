import re

def count_substring(string, sub_string):
    return len([m.start() for m in re.finditer('(?={})'.format(sub_string), string)])

    # for index in xrange(len(string)):
    #     while index+len(sub_string)-1 < len(string):
    #         for subIndex in xrange(len(sub_string)):
    #             if string[index+subIndex]  is sub_string[index+subIndex]:
    #                 totalCount += 1
    # for index in xrange(len(string)-len(sub_string)):
    #     if string[index] == sub_string[0] and string[index+1] == sub_string[1] and string[index+2] == sub_string[2]:
    #         count += 1
    # return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count