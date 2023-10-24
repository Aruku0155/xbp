import random

# 1から100までのランダムな数を選ぶ
target_number = random.randint(1, 9)

# プレイヤーにゲームの説明を表示
print("1から9までの数を当ててください。")

# プレイヤーが正しい数を当てるまで繰り返す
attempts = 0
while True:
    try:
        # プレイヤーに数を入力させる
        guess = int(input("数を入力してください: "))
        attempts += 1

        # プレイヤーの予想を評価する
        if guess < target_number:
            print("bad")
        elif guess > target_number:
            print("bad")
        else:
            print(f"おめでとう！！your winner{target_number} が答えです。{attempts}回目で当てました！")
            break

    except ValueError:
        print("無効な入力です。整数を入力してください。")

# ゲーム終了

