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
            self.alg_pass(False)
            #print(self)
            #print("\n"*8)
            self.curr_pass += 1

        while self.curr_pass < 10:
            self.alg_pass(True)
            self.curr_pass += 1

        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height-1:
                    self.dungeon[i][j] = 0
                elif j == 0 or j == self.width-1:
                    self.dungeon[i][j] = 0
        
        #print(self)

    def neighbors(self, ext, row, col):
        count = 0
        if not ext:
            for dis_h in [-1, 0, 1]:
                for dis_w in [-1, 0, 1]:
                    if self.isInRange(row+dis_h, col+dis_w):
                        #print(row, col, dis_h, dis_w)
                        if self.dungeon[row+dis_h][col+dis_w] == 1:
                            count += 1
        else:
            for dis_h in [-2, -1, 0, 1, 2]:
                for dis_w in [-2, -1, 0, 1, 2]:
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
                no = rand.randint(0, 11)
                if no in range(0,4):

                    self.dungeon[i].insert(j, 0)
                elif no in range(4,11):
                    self.dungeon[i].insert(j, 1)

    def alg_pass(self, polish):
        #0 wall
        #1 open
        new_dung = [[0 for x in range(self.height)] for y in range(self.width)]        
        
        if not polish:
            for i in range(self.height):
                for j in range(self.width):
                    adj = self.neighbors(False, i, j)
                    adj_ext = self.neighbors(True, i, j)
                    #birth threshold
                    if adj >= 5 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    elif adj_ext < 2 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    else:
                        new_dung[i].insert(j, 1)
        else:
            for i in range(self.height):
                for j in range(self.width):
                    adj = self.neighbors(False, i, j)
                    adj_ext = self.neighbors(True, i, j)
                    #birth threshold
                    if adj >= 6 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    elif adj_ext <= -1 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    else:
                        new_dung[i].insert(j, 1)

            if not polish:
                for _ in range(400):
                    i = rand.randint(0, self.height-1)
                    j = rand.randint(0, self.width-1)

                    adj = self.neighbors(False, i, j)
                    adj_ext = self.neighbors(True, i, j)
                    #birth threshold
                    if adj >= 5 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    elif adj_ext <= -1 and self.dungeon[i][j] == 1:
                        new_dung[i].insert(j, 0)
                    else:
                        new_dung[i].insert(j, 1)

        self.dungeon = deepcopy(new_dung)

    def __str__(self):
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                #print(i, j)
                if self.dungeon[i][j] == 0:
                    out += "#"
                elif self.dungeon[i][j] == 1:
                    out += " "
            out += "\n"
        return out

    def get_map(self):
        return self.dungeon
    
