if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m = 0
    i = 0
    while True:
        try:
            if arr[i] == m:
                arr.remove(arr[i])
            else:
                m = arr[i]
                i += 1
        except:
            break

    print(arr[len(arr) - 2])