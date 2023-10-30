import random

def main():
    target_number = random.randint(1, 9)
    attempts = 0
    max_attempts = 3

    print("1から9の数を当ててください。3回以内に正解しなければ失格です。")

    while attempts < max_attempts:
        try:
            guess = int(input("予想する数字を入力してください: "))
        except ValueError:
            print("無効な入力です。整数を入力してください。")
            continue

        if guess < 1 or guess > 9:
            print("1から9の範囲内で予想してください。")
            continue

        attempts += 1

        if guess == target_number:
            print(f"おめでとうございます！正解です。{attempts}回目で当てました。")
            break
        else:
            if attempts < max_attempts:
                print("不正解です。もう一度トライしてください。")

    if attempts >= max_attempts:
        print(f"失格です。正解は{target_number}でした。")

if __name__ == "__main":
    main()
