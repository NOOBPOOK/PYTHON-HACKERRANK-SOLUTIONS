# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = list(input().split())
j = 0
for i in range(n):
    so = list(input().split())
    j += int(so[m.index("MARKS")])
print(j / n)
