s = input()
ans = ""
for chr in s:
    if chr == "B":
        if ans != []:
            ans = ans[:-1]
    else:
        ans += chr
print(ans)
