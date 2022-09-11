def average(array):
    # your code goes here
    arr = set(array)
    avg = 0
    for i in arr:
        avg += i
    return ("{:.3f}".format(avg / len(arr)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)