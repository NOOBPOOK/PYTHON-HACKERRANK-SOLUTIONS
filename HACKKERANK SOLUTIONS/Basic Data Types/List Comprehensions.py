if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print("[",end="")
    for i in range(x+1):
        chk = [0,0,0]
        chk[0] = i
        for j in range(y+1):
            chk[1] = j
            for k in range(z+1):
                chk[2] = k
                if sum(chk) != n:
                    print(chk,end="")
                    if k != z or i != x or j != y:
                        print(",",end=" ")
    print("]")
