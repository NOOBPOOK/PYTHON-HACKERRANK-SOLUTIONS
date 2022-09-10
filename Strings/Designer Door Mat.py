# Enter your code here. Read input from STDIN. Print output to STDOUT
count = 1


def slash(count):
    d = ".|." * (count)
    return d


n = input().split()
for i in range(int(n[0])):
    if i == int(n[0]) // 2:
        print("WELCOME".center(int(n[1]), "-"))
        break
    else:
        print(slash(count).center(int(n[1]), "-"))
        count += 2

count -= 2
for j in range(1, int(n[0]) // 2 + 1):
    print(slash(count).center(int(n[1]), "-"))
    count -= 2