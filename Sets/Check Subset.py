# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0,n):
    n1 = int(input())
    s1 = set(map(int, input().split()))
    n2 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    if len(s1) == len(s1.intersection(s2)):
        print("True")
    else:
        print("False")
