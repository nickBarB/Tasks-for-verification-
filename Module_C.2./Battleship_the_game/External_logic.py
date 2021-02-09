from internal_logic.main_classes import*
from internal_logic.main_check import*
from random import randint

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Attack coordinates: {d.x+1} {d.y+1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Attack coordinates: ").split()

            if len(cords) != 2:
                print(" Captain, the target coordinates are incorrect! \nWe need two coordinates! ")
                continue
            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print(" Captain, the target coordinates are incorrect! \nWe need digital coordinates! ")
                continue
            x, y = int(x), int(y)
            return Dot(x-1, y-1)

class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print(
            f"{'-'*28}\n\tGreetings Captain,\n\twe have a battle ahead!\n{'-'*28}"
            f"\n\tOrders in Target\n\tCoordinate Format: x y."
        )


    def loop(self):
        num = 0
        while True:
            print("-"*28)
            print("Our Fleet")
            print(self.us.board)
            print("-"*28)
            print("Enemy Fleet ")
            print(self.ai.board)
            if num % 2 == 0:
                print("-"*28)
                print("Your order, captain.")
                repeat = self.us.move()
            else:
                print("-"*28)
                print("Enemy attack.")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 28)
                print("Congratulations, captain!")
                break

            if self.us.board.count == 7:
                print("-" * 28)
                print("We will not surrender alive!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

