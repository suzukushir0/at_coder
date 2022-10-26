n = int(input())
s = input()
x, ans = 0, 0
for i in range(n):
    if s[i] == "I":
        x += 1
    elif s[i] == "D":
        x -= 1
    if ans < x:
        ans = x
print(ans)
