import random

def main():
    # 当たりの数字をランダムに選ぶ
    winning_number = random.randint(1, 9)

    print("1から9までの数字があります。1つだけが当たりです。当たりの数字を当ててください！")

    while True:
        try:
            guess = int(input("予想する数字を入力してください: "))
            if guess < 1 or guess > 9:
                print("1から9の数字を選んでください。")
                continue
        except ValueError:
            print("無効な入力です。整数を入力してください。")
            continue

        if guess == winning_number:
            print(f"おめでとうございます！当たりの数字は {winning_number} でした。")
            break
        else:
            print("はずれです。もう一度試してみてください。")

if __name__ == "__main__":
    main()
