if __name__ == '__main__':
    s = input()
    alpha = False
    num = False
    upper = False
    lower = False
    alnum = False
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isnumeric():
            num = True
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
    print(f"{alnum}\n{alpha}\n{num}\n{lower}\n{upper}")