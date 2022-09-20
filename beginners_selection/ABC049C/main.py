"""
ABC049C - 白昼夢

問題文
英小文字からなる文字列 S が与えられます。
Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。
・T の末尾に dream dreamer erase eraser のいずれかを追加する。

制約
・1≦∣S∣≦10^5
・S は英小文字からなる。

入力
入力は以下の形式で標準入力から与えられる。
S

出力
S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。
"""
S = input()
S = S.replace("eraser", "")
S = S.replace("erase", "")
S = S.replace("dreamer", "")
S = S.replace("dream", "")

if S == 0:
    print("YES")
else:
    print("NO")

"""
ここまで縮められる。。。らしい
s=input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
print("YES" if len(s)==0 else "NO")
"""
