"""
ABC083B - Some Sums

問題文
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

制約
・1≤N≤10^4
・1≤A≤B≤36
・入力はすべて整数である

入力
入力は以下の形式で標準入力から与えられる。
N A B

出力
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。
"""
# input要素の取得（N A B）
n, a, b = map(int, input().split())
# 総和用変数
ans = 0

# 0~(n+1)(N以下)をループ
for i in range(n+1):
    # 各桁の和:iのString->listで分割->map;iteration->list化し合算
    if a <= sum(list(map(int, list(str(i))))) <= b:
        ans += i

print(ans)
