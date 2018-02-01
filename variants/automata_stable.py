import random as rand
from copy import deepcopy

class Dungeon:
    def __init__(self):
        self.dungeon = None
        self.curr_pass = 0

    def init(self, h, w):
        self.dungeon = [[0 for x in range(h)] for y in range(w)] 

        self.height, self.width = h, w

    def generate(self):
        self.randomize()
        while self.curr_pass < 4:
            self.alg_pass()
            #print(self)
            #print("\n"*8)
            self.curr_pass += 1

        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height-1:
                    self.dungeon[i][j] = 0
                elif j == 0 or j == self.width-1:
                    self.dungeon[i][j] = 0

    def neighbors(self, row, col):
        count = 0

        for dis_h in [-1, 0, 1]:
            for dis_w in [-1, 0, 1]:
                if self.isInRange(row+dis_h, col+dis_w):
                    #print(row, col, dis_h, dis_w)
                    if self.dungeon[row+dis_h][col+dis_w] == 1:
                        count += 1

        return count

    def isInRange(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width

    def randomize(self):
        for i in range(self.height):
            for j in range(self.width):
                self.dungeon[i].insert(j, rand.randint(0, 1))

    def alg_pass(self):
        new_dung = [[0 for x in range(self.height)] for y in range(self.width)]

        for i in range(self.height):
            for j in range(self.width):
                adj = self.neighbors(i, j)
                if adj >= 4 and self.dungeon[i][j] == 1:
                    new_dung[i].insert(j, 1)
                elif adj >= 5 and self.dungeon[i][j] == 0:
                    new_dung[i].insert(j, 1)
                else:
                    new_dung[i].insert(j, 0)

        self.dungeon = deepcopy(new_dung)

    def __str__(self):
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.dungeon[i][j] == 0:
                    out += "#"
                elif self.dungeon[i][j] == 1:
                    out += " "
            out += "\n"
        return out

    def get_map(self):
        return self.dungeon
        
