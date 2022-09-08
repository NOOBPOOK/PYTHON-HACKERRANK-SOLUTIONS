def swap_case(s):
    j = ""
    for i in s:
        if i.isupper():
            j+=str(i.lower())
        else:
            j+=str(i.upper())
    return j

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)