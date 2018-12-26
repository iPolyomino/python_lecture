# coding: utf-8

from random import randint


def main():
    a_tips = 21
    b_tips = 21
    for _ in range(5):
        dice = throwDice()
        if dice == 7:
            a_tips += 7
        else:
            a_tips -= abs(dice - 7)
        print("a のチップは{}枚".format(a_tips))
        if a_tips <= 0:
            break

        dice = throwDice()
        if dice == 7:
            b_tips += 7
        else:
            b_tips -= abs(dice - 7)
        print("b のチップは{}枚".format(b_tips))
        if b_tips <= 0:
            break

    if a_tips > b_tips:
        print("aの勝ち")
    elif a_tips == b_tips:
        print("引き分け")
    else:
        print("bの勝ち")


def throwDice():
    return randint(1, 6) + randint(1, 6)


if __name__ == "__main__":
    main()
