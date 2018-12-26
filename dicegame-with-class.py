# coding: utf-8

from random import randint


class Player:
    def __init__(self, name="プレイヤー"):
        self.name = name
        self.tips = 21

    def throw(self):
        dice = self.throwDice()
        if dice == 7:
            self.tips += 7
        else:
            self.tips -= abs(dice - 7)
        print("{} のチップは{}枚".format(self.name, self.tips))

    def throwDice(self):
        return randint(1, 6) + randint(1, 6)


def main():
    player_a = Player("a")
    player_b = Player("b")

    for _ in range(5):
        player_a.throw()
        player_b.throw()
        if player_a.tips <= 0 or player_b.tips <= 0:
            break

    if player_a.tips > player_b.tips:
        print("a の勝ち")
    elif player_a.tips == player_b.tips:
        print("引き分け")
    else:
        print("b の勝ち")


if __name__ == "__main__":
    main()
