# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set()
for i in range(n):
    cou = input()
    s.add(cou)
print(len(s))