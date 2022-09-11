# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

n = list(map(int, input().split()))
m = list(map(int, input().split()))
for i in list(product(n, m)):
    print(i, end=" ")