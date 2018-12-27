# coding: utf-8

from random import randint


def main():
    a_chip = 21
    b_chip = 21
    for _ in range(5):
        dice = throwDice()
        if dice == 7:
            a_chip += 7
        else:
            a_chip -= abs(dice - 7)
        print("a のチップは{}枚".format(a_chip))
        if a_chip <= 0:
            break

        dice = throwDice()
        if dice == 7:
            b_chip += 7
        else:
            b_chip -= abs(dice - 7)
        print("b のチップは{}枚".format(b_chip))
        if b_chip <= 0:
            break

    if a_chip > b_chip:
        print("aの勝ち")
    elif a_chip == b_chip:
        print("引き分け")
    else:
        print("bの勝ち")


def throwDice():
    return randint(1, 6) + randint(1, 6)


if __name__ == "__main__":
    main()
