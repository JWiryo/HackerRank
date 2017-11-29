import sys

if __name__ == '__main__':
    n = int(raw_input())

    for i in xrange(n):
        sys.stdout.write(str(i+1));
    sys.stdout.flush();