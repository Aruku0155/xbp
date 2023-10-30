import random

# ランダムな1から9の数字を生成
target_number = random.randint(1, 9)

# プレイヤーに当てる数字を入力してもらうループ
while: max attempts=3
    try:
        guess = int(input("1から9までの数字を入力する: "))
        if 1 <= guess <= 9:
            break
        else:
            print("1から9までの有効な数字を入力する。")
    except ValueError:
        print("数字を入力する。")

# 当てるまで繰り返す
attempts = 0
while :max_attempts=3
    attempts += 1
    if guess == target_number:
        print(f"you win !!{attempts}回目で正解です。正解の数字は{target_number}です。")
        break
   
     # 次の予想を入力
    try:
        guess = int(input("他の数字です: "))
    except ValueError:
        print("数字を入力する。")
 








