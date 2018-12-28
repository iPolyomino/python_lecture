# coding: utf-8

from random import randint


def throwDice():
    return randint(1, 6) + randint(1, 6)


def judge(dice):
    if dice < 7:
        return "low"
    elif dice == 7:
        return "even"
    else:
        return "high"


def game(chip):
    print("Your chip : {}".format(chip))
    print("BET >> ", end="")
    bet = int(input())
    while bet < 1 or chip < bet:
        print("Please enter again.")
        bet = int(input())
    chip -= bet

    print("Higher than 7 ?")
    print("high, low or even >> ", end="")
    high_or_low = input()
    while not high_or_low in {"high", "low", "even"}:
        print("Please enter again.")
        high_or_low = input()

    dice = throwDice()
    print("Result : {}".format(dice))
    if judge(dice) == high_or_low:
        print("Great!")
        if dice == 7:
            chip += bet * 5
        else:
            chip += bet * 2
    return chip


def main():
    chip = 20
    for _ in range(5):
        chip = game(chip)
        if chip == 0:
            print("Game Over")
            return
    if chip > 20:
        print("You Win")
    else:
        print("You lose")


if __name__ == "__main__":
    main()
