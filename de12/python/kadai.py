import random

def main():
    target_number = random.randint(1, 9)
    max_attempts = 3
    attempts = 0

    print("1から9までの数字を当てるゲームです。")
    print(f"3回以内にランダムな数字を当ててください。")

    while attempts < max_attempts:
        guess = int(input("予想した数字を入力してください: "))

        if guess == target_number:
            print("おめでとうございます！正解です。")
            break
        else:
            print("不正解です。")
            attempts += 1

    if attempts == max_attempts:
        print(f"残念！正解は {target_number} でした。")

if __name__ == "__main":
    main()

