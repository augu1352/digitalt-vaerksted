import tkinter as tk
#from tkinter import messagebox as msgbx

#lobal canv = tk.Canvas()


class main:
    def __init__(self, bg, rootgeo, canvwidth, canvheight):
        self.root = tk.Tk()
        self.root.geometry(rootgeo)
        self.root.mainloop()
        self.bg = bg


    def update():
        pass


    def createCircle(x, y, r, color, canvas):
        player = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
        return player

    def window(bg):
        canv = tk.Canvas(self.root, bg=bg, width=canvwidth, height=canvheight)
        #player = canv.create_oval(100, 100, 250, 200, fill="blue")
        createCircle(50, 50, 50, "blue", canv)
        canv.pack()
        self.root.mainloop()
        # player.pack()
        canv.pack()



m = main("red", "400x400", 400, 400)
m.window(m.bg)
