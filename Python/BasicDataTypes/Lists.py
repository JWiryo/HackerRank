if __name__ == '__main__':
    N = int(raw_input())
    outputList = [];
    for i in xrange(N):
        inputString = str(raw_input()).split(" ");
        if inputString[0] == "insert":
            outputList.insert(int(inputString[1]), int(inputString[2]))
        elif inputString[0] == "print":
            print outputList
        elif inputString[0] == "remove":
            outputList.remove(int(inputString[1]))
        elif inputString[0] == "append":
            outputList.append(int(inputString[1]))
        elif inputString[0] == "sort":
            outputList.sort()
        elif inputString[0] == "pop":
            outputList.pop()
        elif inputString[0] == "reverse":
            outputList.reverse()
