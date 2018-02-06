import tkinter as tk


class Player:
    playerCount = 0
    playerList = []
    def __init__(self, name, width, height, color):
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        Player.playerCount += 1

class GUI:
    guiCount = 0
    def __init__(self, rootGeo, bgColor, canvWidth, canvHeight):
        self.root = tk.Tk()
        self.root.geometry(rootGeo)
        self.canv = tk.Canvas(self.root, bg=bgColor, width=canvWidth, height=canvHeight)

        for p in Player.playerList:
            self.canv.create_oval(p.width, p.height, 250, 200, fill=p.color, tags=p.name)

        self.canv.pack()
        self.root.mainloop()
        GUI.guiCount += 1

    def AddPlayerToCanvas(canvas, player):
        canvas.create_oval(100, 100, 250, 200, fill="blue")

a = Player("x", 100, 100, "white")
b = Player("y", 150, 100, "blue")
c = Player("z", 200, 100, "green")

Player.playerList.append(a)
Player.playerList.append(b)
Player.playerList.append(c)

g = GUI("400x400", "red", 400, 400)
canv = g.canv
#g.AddPlayerToCanvas(canv, a)

#a = Player(100, 100, "red")
#b = Player(100, 100, "blue")
#c = Player(100, 100, "green")

#print(len(Player.playerList))

#print(b.color)
#print(a.color)
#print(c.color)
