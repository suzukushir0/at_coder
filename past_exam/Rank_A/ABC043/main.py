""" ABC043 A - キャンディーとN人の子供イージー """

n = int(input())
ans = 0
for i in range(n + 1):
    ans += i
print(ans)
