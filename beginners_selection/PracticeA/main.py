"""
PracticeA - Welcome to AtCoder

問題文
高橋君はデータの加工が行いたいです。
整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。

制約
1≤a,b,c≤1,000
1≤∣s∣≤100

入力
a
b c
s

出力
a+b+c と s を空白区切りで 1 行に出力せよ
"""

# 整数の入力
a = int(input())

# 半角スペース区切りの入力
b, c = map(int, input().split())

# 文字列の入力
s = input()

# 出力
print(f"{a+b+c} {s}")
