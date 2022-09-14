"""
ABC081B - Shift only

問題文
黒板に N個の正の整数 A1, ..., ANが書かれています.

すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
    ・黒板に書かれている整数すべてを, 2で割ったものに置き換える.
すぬけ君は最大で何回操作を行うことができるかを求めてください．

制約
1≤N≤200
1 ≤ Ai ≤ 10^9

入力
入力は以下の形式で標準入力から与えられる。
N
A1 A2 ... AN

出力
すぬけ君は最大で何回操作を行うことができるかを出力せよ．
"""

n = int(input())
a = list(map(int, input().split()))
count  = 0

# リスト内がすべて偶数の場合、ループ
while all(i%2==0 for i in a):
    count += 1
    a = [j/2 for j in a]

print(count)

'''
# 別解： 2進数に変換する
ans = float('inf')
for i in a:
    ans = min(ans, len(bin(i) - bin(i).rfind('1') - 1))
print(ans)
'''
