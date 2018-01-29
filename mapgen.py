import random as rand

class Dungeon:
    def __init__(self):
        self.dungeon = None
        self.fresh = True

        self.height, self.width = 0, 0
    def init(self, h, w):
        self.dungeon = [["#" for x in range(w)] for y in range(h)] 

        self.height, self.width = h, w

    def gen_rm(self, orient=None, height=4, width=6):
        self.flag = False
        '''
        ORIENT
        0 top
        1 right
        2 botom
        3 left
        '''
        if self.fresh:
            mid_h = int(self.height/2-height/2)-2
            mid_w = int(self.width/2-width/2)-4

            for i in range(mid_h, mid_h+height):
                for j in range(mid_w, mid_w+width):
                    self.dungeon[i][j] = " "
                    self.flag = True

        else:
            border = False
            while not border:
                rh, rw = rand.choice(range(self.height)[2:-2]), rand.choice(range(self.width)[2:-2])
                adj_tile = self.adj(rh, rw)
                
                #test begin
                #if adj_tile != None:
                    #print(adj_tile)

                #test end

                if (adj_tile):
                    border = True
                    #print(rh, rw)
                    #rh += 2
                    #rw += 2
                    dis_h = adj_tile[2]
                    dis_w = adj_tile[3]
                    self.dungeon[rh][rw] = "W"

            clear_space = True
            if dis_h < 0:
                if rh-height < 0 or rw+width > self.width-1:
                    clear_space = False
                else:
                    for i in range(rh-height, rh):
                        for j in range(rw, rw+width):
                            if(self.dungeon[i][j] not in ["#", "W"]):
                                clear_space = False
                                break

            elif dis_w < 0:
                if rh-height < 0 or rw-width < 0:
                    clear_space = False
                else:
                    for i in range(rh-height, rh):
                        for j in range(rw-width, rw):
                            if(self.dungeon[i][j] not in ["#", "W"]):
                                clear_space = False
                                break
            
            else:
                if rh+height > self.height-1 or rw+width > self.width-1:
                    clear_space = False
                else:
                    for i in range(rh, rh+height):
                        for j in range(rw, rw+width):
                            if(self.dungeon[i][j] not in ["#", "W"]):
                                clear_space = False
                                break

            if clear_space:
                if dis_h < 0:
                    for i in range(rh-height, rh):
                        for j in range(rw, rw+width):
                            self.dungeon[i][j] = " "
                            self.flag = True
                elif dis_w < 0:
                    for i in range(rh-height, rh):
                        for j in range(rw-width, rw):
                            self.dungeon[i][j] = " "
                            self.flag = True
                
                else:
                    for i in range(rh, rh+height):
                        for j in range(rw, rw+width):
                            self.dungeon[i][j] = " "
                            self.flag = True

            for i in range(self.height):
                for j in range(self.width):
                    if self.dungeon[i][j] == "W":
                        if clear_space:
                            self.dungeon[i][j] = " "
                        else:
                            self.dungeon[i][j] = "#"
        
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height or i == self.height-1:
                    self.dungeon[i][j] = "#"
                elif j == 0 or j == self.width or j == self.width-1:
                    self.dungeon[i][j] = "#"

        self.fresh = False
        return self.flag

    def adj(self, rh, rw):
        if(self.dungeon[rh][rw] == "#" and rh+1 < self.height-1 and rh-1 > 0 and rw+1 < self.width-1 and rw-1 > 0):
            for dis_h in [-1, 1]:
                for dis_w in [-1, 1]:
                    if self.dungeon[rh+dis_h][rw+dis_w] == " ":
                        return [rh+dis_h, rw+dis_w, dis_h*-1, dis_w*-1]

    def __str__(self):
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                out += self.dungeon[i][j]
            out += "\n"
        return out

    def get_map(self):
        return self.dungeon



def test():
    d = Dungeon()
    d.init(20, 50)
    d.gen_rm()
    i = 0
    while i < 10:
        if(d.gen_rm(rand.randint(3, 7), rand.randint(3, 7))):
            i += 1
    print(d)

