class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [["O"]*size for _ in range(size)]
        self.busy = []
        self.ships = []
        # self.allowed = []
        #for i in range (size):
            #for j in range (size):
                #self.allowed.append(Dot(i,j))

    def add_ship(self, ship):
        for d in siip.dots:
            self.field[d.x][d.y] = "■"


B = Board()

print(B.field)
