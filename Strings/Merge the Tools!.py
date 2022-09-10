import textwrap


def merge_the_tools(string, k):
    # your code goes here
    # vg = int(len(string)/((string/)))
    g = textwrap.TextWrapper(width=k)
    h = g.wrap(string)
    i = 0
    m = 0
    for f in h:
        b = list(dict.fromkeys(list(f)))
        print(''.join(b))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)