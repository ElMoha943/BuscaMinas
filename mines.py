import random
from tkinter import *
import math

root = Tk()
root.title("Busca Minas")

rows = 5
columns = 5


class Board:
    def __init__(self):
        self.cells = [ [0]*columns for i in range(rows)]
    def __getitem__(self, i):
        return self.cells
    def clear(self):
        for c in self.cells:
            for cc in c:
                cc.btn.destroy()
    def populate(self):
        for i in range(rows):
            root.grid_rowconfigure(i,  weight =1)
            root.grid_columnconfigure(i,  weight =1)
            for j in range(columns):
                self.cells[i][j] = Cell(i, j)

class Cell:
    def button_click(self,x):
        print(f'Coords: {x}')
        if(self.mine):
            self.btn.config(text="X", state=DISABLED)
            """ board.clear() """
        else:
            cont = count(self, board)
            self.btn.config(text=f'{cont}', state=DISABLED)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = random.getrandbits(1)
        self.revealed = False
        self.btn = Button(root, text=f'{x} - {y}', padx=40, pady=20, command=lambda: self.button_click(f'{x} - {y}'))
        self.btn.grid(row=y, column=x, sticky=NSEW)

def count(celda, boardd):
    cont = 0
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if(boardd.cells[celda.x + i][celda.y + j].mine and (celda.x + i >= 0) and (celda.y + j >= 0)):
                    cont+=1 
                    print(f'Celda: {celda.x + i} - {celda.y + j}\nCont: {cont}')
            except:
                pass
    return cont

board = Board()
board.populate()

root.mainloop()
