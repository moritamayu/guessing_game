import numpy as np

num = np.random.randint(100, 1000, (1, 1))
##print(num)

print("三桁の数字を入力してください．")
num_player = int (input())

if num_player==num:
    print("正解です！")

else:
    print("不正解です．")
    print("ヒント１：", end="")
    if num_player>num:
        print("もっと小さい数字です．")
    else:
        print("もっと大きい数字です")