import random as rand

class Populate:
    def __init__(self, dungeon):
        self.dungeon = dungeon

    def __str__(self):
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                out += self.dungeon[i][j]
            out += "\n"
        return out

    def get_map(self):
        return self.dungeon