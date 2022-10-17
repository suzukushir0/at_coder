w, h, n = map(int, input().split())
list = []
for _ in range(n):
    x, y, a = input().split()
    list.append([int(x), int(y), int(a)])

left = 0
right = w
down = 0
up = h

for i in list:
    if i[2] == 1:
        if left < i[0]:
            left = i[0]
    if i[2] == 2:
        if right > i[0]:
            right = i[0]
    if i[2] == 3:
        if down < i[1]:
            down = i[1]
    if i[2] == 4:
        if up > i[1]:
            up = i[1]

line = right - left
row = up - down

if line < 0 or row < 0:
    print(0)
else:
    print(row * line)
