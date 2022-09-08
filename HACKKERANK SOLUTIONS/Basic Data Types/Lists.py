if __name__ == '__main__':
    li = []
    N = int(input())
    for i in range(N):
        cmd = input().split()
        if cmd[0] == "insert":
            li.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            li.remove(int(cmd[1]))
        elif cmd[0] == "append":
            li.append(int(cmd[1]))
        elif cmd[0] == "reverse":
            li.reverse()
        elif cmd[0] == "pop":
            li.pop()
        elif cmd[0] == "sort":
            li.sort()
        elif cmd[0] == "print":
            print(li)