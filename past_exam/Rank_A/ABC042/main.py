""" ABC042 A - 和風いろはちゃんイージー """

list = sorted(list(map(int, input().split())), reverse=True)
if list[0] == 7:
    if list[1] == list[2] == 5:
        print("YES")
        exit()
print("NO")
