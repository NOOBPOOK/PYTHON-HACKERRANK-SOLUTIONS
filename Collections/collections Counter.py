# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
size = list(map(int, input().split()))
csnm = int(input())
total = 0
for i in range(csnm):
    ord = list(map(int, input().split()))
    if ord[0] in size:
        total += int(ord[1])
        size.remove(ord[0])
    else:
        pass

print(total)
