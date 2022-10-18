""" TLE
def main():
    a, b, x = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        if i % x == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
"""


def main():
    def f(n, d):
        if -1 == n:
            return 0
        return (n // x) + 1

    a, b, x = map(int, input().split())
    print(f(b, x) - f(a - 1, x))


if __name__ == "__main__":
    main()
