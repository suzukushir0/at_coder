"""
ABC086C - Traveling

問題文
シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。
AtCoDeerくんの旅行プランでは、時刻 0 に 点 (0,0) を出発し、
1 以上 N 以下の各i に対し、時刻 tiに 点 (xi ,yi) を訪れる予定です。
AtCoDeerくんが時刻 t に 点 (x,y) にいる時、 時刻 t+1 には
点 (x+1,y), (x−1,y), (x,y+1), (x,y−1) のうちいずれかに存在することができます。
その場にとどまることは出来ないことに注意してください。
AtCoDeerくんの旅行プランが実行可能かどうか判定してください。

制約
・1 ≤ N  ≤ 10^5
・0 ≤ xi ≤ 10^5
・0 ≤ yi ≤ 10^5
・1 ≤ ti ≤ 10^5
・ti < ti+1(1 ≤ i ≤ N−1)
・入力は全て整数

入力
入力は以下の形式で標準入力から与えられる。
N
t1 x1 y1
t2 x2 y2
​.
.
.
tN xN yN

出力
旅行プランが実行可能ならYesを、不可能ならNoを出力してください。
"""
N = int(input())
T, X, Y = 0, 0, 0
# マンハッタン距離：直角移動の最短距離
# http://www.otupy.net/archives/39930126.html
# https://kagglenote.com/misc/various-distance/
for i in range(N):
    t, x, y = map(int, input().split())
    # マンハッタン距離
    dist = abs(x - X) + abs(y - Y)
    time = T + t

    if time % 2 != dist % 2 or time < dist:
        print("No")
        exit()
    T, X, Y = t, x, y

print("Yes")

"""
失敗！　なぜだ。。。
"""
