list = list(map(int, input().split()))
max = max(list)
list.remove(max)

if max == sum(list):
    print("Yes")
else:
    print("No")

"""
a == b + c or
b == a + c or
c == a + b
"""
