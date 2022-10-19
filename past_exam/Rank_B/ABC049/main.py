"""コード短い
h, w = map(int, input().split())
for a in [input() for _ in range(h)]:
    print(f"{a}\n{a}")
"""

""" はやい """
h, w = map(int, input().split())
c = [input() for _ in range(h)]

for a in c:
    print(a)
    print(a)
