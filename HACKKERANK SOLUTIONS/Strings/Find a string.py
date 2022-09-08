def count_substring(string, sub_string):
    b = len(sub_string)
    x = 0
    j = len(string)
    string += "      "
    n = 0
    m = 0
    for i in range(0, j):
        exp = ""
        for d in range(0, b):
            exp += string[n]
            n += 1
        if exp == sub_string:
            x += 1
        m += 1
        n = m
    return x


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)