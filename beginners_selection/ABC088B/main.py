"""
ABC088B - Card Game for Two
問題文
N 枚のカードがあります. i 枚目のカードには, aiという数が書かれています.
Alice と Bob は, これらのカードを使ってゲームを行います.
ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます.
Alice が先にカードを取ります.
2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります.
2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

制約
N は 1 以上 100 以下の整数
ai(1≤i≤N) は 1 以上 100 以下の整数

入力
入力は以下の形式で標準入力から与えられる.
N
a1 a2 a3 ... aN

出力
両者が最適な戦略を取った時, Alice は Bob より何点多く取るかを出力してください.
"""

N = input()
A = sorted(list(map(int, input().split())), reverse=True)
print(sum(A[::2]) - sum(A[1::2]))
"""リファクタ前
N = input()
A = list(map(int, input().split()))
sorted(A, reverse=True)
Alice = sum(A[::2])
Bob = sum(A[1::2])
print(Alice - Bob)
"""
