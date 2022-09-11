# Enter your code here. Read input from STDIN. Print output to STDOUT
num = str(input())
k = 0
count = 1
for i in num:
    try:
        if i != num[k+1]:
            print((int(count), int(i)),end = " ")
            count = 1
        else:
            count+=1
        k+=1
    except:
        print((int(count), int(i)))
