import automata
import tkinter as tk

class Rectangle(object):
    def __init__(self, canvas, coords, fill, outline=None):
        self.canvas = canvas
        self.fill = fill
        self.outline = outline if outline is not None else self.fill
        self.canvas_id = self.canvas.create_rectangle(
            coords, outline=self.outline, fill=self.fill)

def test():
    h = 250
    w = 250

    t = tk.Tk()
    c = tk.Canvas(t, height=h*3+3, width=w*3+3)

    a = automata.Dungeon()
    a.init(h, w)
    a.generate()
    for i in range(a.height):
        for j in range(a.width):
            if a.dungeon[i][j] == 0:
                Rectangle(c, (i*3, j*3, i*3+3, j*3+3), "black")

    c.pack()

    t.mainloop(n=0)

if __name__ == '__main__':
    test()

