w = input()
d = {}
for ｓ in w:
    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1
for v in d.values():
    if v % 2 == 1:
        print("No")
        exit()
print("Yes")
