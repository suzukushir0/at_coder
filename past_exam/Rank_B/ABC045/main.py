a = list(input())
b = list(input())
c = list(input())
d = {"a": a, "b": b, "c": c}

tmp = "a"
while d[tmp]:
    tmp = d[tmp].pop(0)
print(tmp.upper())
