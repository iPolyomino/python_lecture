# coding: utf-8

from random import randint


class Player:
    def __init__(self, name="プレイヤー"):
        self.name = name
        self.chip = 21

    def throw(self):
        dice = self.throwDice()
        if dice == 7:
            self.chip += 7
        else:
            self.chip -= abs(dice - 7)
        print("{} のチップは{}枚".format(self.name, self.chip))

    def throwDice(self):
        return randint(1, 6) + randint(1, 6)


def main():
    player_a = Player("a")
    player_b = Player("b")

    for _ in range(5):
        player_a.throw()
        player_b.throw()
        if player_a.chip <= 0 or player_b.chip <= 0:
            break

    if player_a.chip > player_b.chip:
        print("a の勝ち")
    elif player_a.chip == player_b.chip:
        print("引き分け")
    else:
        print("b の勝ち")


if __name__ == "__main__":
    main()
