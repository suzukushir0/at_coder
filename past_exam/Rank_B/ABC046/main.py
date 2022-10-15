n, k = map(int, input().split())
if n == 1:
    print(k)
else:
    ans = k
    for _ in range(n - 1):
        ans = ans * (k - 1)
    print(ans)
