# @Time     :   2018-6-21 22:17
# @Author   :   chenzeshenga
# @Email    :   chenzeshenga@163.com
# @File     :   Dice.py
# @Software :   PyCharm
import random


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        print("game started")

    def start_game(self):
        self.player1.cast()
        self.player2.cast()

        player1_dice_list = (self.player1.dices[0], self.player1.dices[1], self.player1.dices[2])
        player2_dice_list = (self.player2.dices[0], self.player2.dices[1], self.player2.dices[2])

        print(player1_dice_list)
        print(player2_dice_list)


class Player:

    def __init__(self, name, sex, *dice):
        self.name = name
        self.sex = sex
        self.dices = dice
        print("player %s" % name)

    # 玩家抛骰子
    def cast(self):
        for dice in self.dices:
            dice.move()

    def guess_dice(self):
        return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))


class Dice:

    def __init__(self, num):
        self.num = 0
        # print("dice num %s" % num)

    # 摇骰子
    def move(self):
        self.num = random.randint(1, 6)
        print(self.num)


d1 = Dice(2)
d2 = Dice(2)
d3 = Dice(2)

dd1 = Dice(2)
dd2 = Dice(2)
dd3 = Dice(2)

player1 = Player("abc", "F", d1, d2, d3)
player2 = Player("bcd", "F", dd1, dd2, dd3)

game1 = Game(player1, player2)

game1.start_game()
