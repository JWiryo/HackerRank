if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    secondLargest = min(arr)
    maxNum = max(arr)
    for i in arr:
        if secondLargest <= i < maxNum:
            secondLargest = i

    print secondLargest;
