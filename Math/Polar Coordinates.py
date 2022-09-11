# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

num = complex(input())
num = cmath.polar(num)
for x in num:
    print(x)
