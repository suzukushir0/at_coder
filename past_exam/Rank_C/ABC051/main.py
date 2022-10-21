def main():
    sx, sy, tx, ty = map(int, input().split())
    w = tx - sx
    h = ty - sy
    ww = w + 1
    wh = h + 1
    ans = "U" * h + "R" * w
    ans += "D" * h + "L" * w
    ans += "L" + "U" * wh + "R" * ww + "D"
    ans += "R" + "D" * wh + "L" * ww + "U"
    print(ans)


if __name__ == "__main__":
    main()
