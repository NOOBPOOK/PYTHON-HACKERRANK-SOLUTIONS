# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
PI = 3.14

n = int(input())
m = int(input())
nm = (pow(n,2)+pow(m,2))
nm = pow(nm, 1/2)
area = (1/4) * n * m
hm = (area*2)/m
gm = (area*2)/n
deg = math.degrees((math.atan(hm/gm)))
print(str(round(deg))+u"\u00b0")

