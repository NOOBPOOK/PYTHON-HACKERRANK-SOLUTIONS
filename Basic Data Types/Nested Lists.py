if __name__ == '__main__':
    # Creating a dict to store values
    py_dic = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in list(py_dic.keys()):
            py_dic[score].append(str(name))
        else:
            py_dic[score] = [str(name)]

    # Finding the 2nd minimum score
    k = sorted(list(py_dic.keys()))
    [print(x) for x in sorted(py_dic[k[1]])]