def print_formatted(number):
    width = len(bin(number))
    for i in xrange(1, int(number)+1):
        print "{} {} {} {}".format(str(i).rjust(width, ' '), oct(i)[1:].rjust(width, ' '), hex(i)[2:].capitalize().rjust(width, ' '), bin(i)[2:].rjust(width, ' '))

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)