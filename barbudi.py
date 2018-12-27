# coding: utf-8

from random import randint


def resultPrint(player, turn, diceResult):
    name = playerName(player, turn)
    print("{} さん：{}".format(name, diceResult))


def playerName(player, turn):
    return player[turn % len(player)]


def judge(resultTuple):
    winningState = {(6, 6), (6, 5), (5, 6), (5, 5), (4, 4)}
    losingState = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
    if resultTuple in winningState:
        return True, "勝ち"
    elif resultTuple in losingState:
        return True, "負け"
    else:
        return False, None


def throwDice():
    return (randint(1, 6), randint(1, 6))


def main():
    turn = 0
    player = ["A", "B"]
    diceResult = throwDice()
    resultPrint(player, turn, diceResult)
    isEnd, state = judge(diceResult)

    while not isEnd:
        turn += 1
        diceResult = throwDice()
        resultPrint(player, turn, diceResult)
        isEnd, state = judge(diceResult)

    name = playerName(player, turn)
    print("{} さんの{}".format(name, state))


if __name__ == "__main__":
    main()
