n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = []
for _ in range(m):
    px.append(list(map(int, input().split())))
for i in range(len(px)):
    c = t.copy()
    c[px[i][0] - 1] = px[i][1]
    print(sum(c))
