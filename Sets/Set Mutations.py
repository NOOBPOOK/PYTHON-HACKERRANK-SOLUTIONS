# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
for h in range(0, m):
    cmd = input().split()
    lst = set(map(int, input().split()))
    if "intersection_update" == str(cmd[0]):
        s1.intersection_update(lst)
    elif "update" == str(cmd[0]):
        s1.update(lst)
    elif "symmetric_difference_update" == str(cmd[0]):
        s1.symmetric_difference_update(lst)
    elif "difference_update" == str(cmd[0]):
        s1 -= lst

print(sum(s1))
