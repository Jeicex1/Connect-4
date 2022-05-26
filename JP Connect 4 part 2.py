from tkinter import *
from tkinter import font

class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=600, height=100)
        mainfont = font.Font(self, size=25, family='MS Sans Serif')  #sets main font information
        self.text = Label(self, text="Yellow's Turn", font=mainfont)
        self.text.grid(sticky=NSEW, pady=20) #The checker will fill the whole grid when you use NSEW. NSEW=north south east west and with sticky it bascially means it sticks to each side
        
class Point(object):
    def __init__(self, x, y, canvas, color="white", background="firebrick3"): #firebrick3 hex code is #cd2626
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.point = self.canvas.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=color,outline="navy")

    def changeColor(self, color):
        self.canvas.itemconfigure(self.point, fill=color) #fills the point pressed with the color
        self.color = color

class Board(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, background="navy") #navy hexcode is #000080
        self.player = 1
        self.color = "gold2" #gold2 hex code is #eec900
        self.placement = []
        self.perm = True
        for height in range(0, 340, int(400/6)): #six rows
            row_list = []
            for width in range(0, 440, int(500/7)): #seven collumns
                row_list.append(Point(width, height, self))   
            self.placement.append(row_list)
        self.bind("<Button-1>", self.detectCol) #button 1 is a left click

    def detectCol(self, event):  
        if self.perm:
            col = int(event.x/71)  #500 (width) / 7 (collumns)
            line = 0
            while line < len(self.placement):            
                if self.placement[0][col].color == "firebrick3" or self.placement[0][0].color == "gold2":
                    break
                if self.placement[line][col].color == "firebrick3" or self.placement[line][col].color == "gold2":
                    self.placement[line-1][col].changeColor(self.color)
                    break
                elif line == len(self.placement)-1:
                    self.placement[line][col].changeColor(self.color)
                    break
                if self.placement[line][col].color != "firebrick3" and self.placement[line][col].color != "gold2":
                    line+=1
            if self.player == 1:
                self.player = 2
                info.text.config(text="Red's Turn")
                self.color = "firebrick3"
            elif self.player == 2:
                self.player = 1
                info.text.config(text="Yellow's Turn")
                self.color = "gold2"
            self.Horizontal() #checks for horizontal win 
            self.Vertical() #checks for Vertical win 
            self.Diagonal1() #checks for diagonal right win 
            self.Diagonal2() #checks for diagonal left win 

#all of the win conditions can probably be a bit more concise, like i had it in the part 1, but some bugs made it seem more reasonable to divide it into colors. 
    def Horizontal(self): #checks for horizontal win 
        height = 0
        while(height < len(self.placement)):
            width = 0
            while(width < 3): #checks for the same value in the same row
                if(self.placement[height][width].color == self.placement[height][width+1].color == self.placement[height][width+2].color == self.placement[height][width+3].color == "firebrick3"):
                    info.text.config(text="Red Wins!")
                    self.perm = False
                    break
                elif(self.placement[height][width].color == self.placement[height][width+1].color == self.placement[height][width+2].color == self.placement[height][width+3].color == "gold2"):
                    info.text.config(text="Yellow Wins!")
                    self.perm = False
                    break
                width +=1
            height += 1

    def Vertical(self): #checks for vertical win
        height = 0
        while(height < 3):
            width = 0 #checks for the same value in the same column
            while(width < len(self.placement[height])):
                if(self.placement[height][width].color == self.placement[height+1][width].color == self.placement[height+2][width].color == self.placement[height+3][width].color == "firebrick3"):
                    info.text.config(text="Red Wins!")
                    self.perm = False
                    break
                elif(self.placement[height][width].color == self.placement[height+1][width].color == self.placement[height+2][width].color == self.placement[height+3][width].color == "gold2"):
                    info.text.config(text="Yellow Wins!")
                    self.perm = False
                    break
                width+=1
            height+=1

    def Diagonal1(self):  #check for diagonal right wins
        height = 0
        while(height < 3):
            width = 0
            while(width < 3): #checks for the same value going up and to the right once
                if(self.placement[height][width].color == self.placement[height+1][width+1].color == self.placement[height+2][width+2].color == self.placement[height+3][width+3].color == "firebrick3"):
                    info.text.config(text="Red Wins!")
                    self.perm = False
                    break 
                elif(self.placement[height][width].color == self.placement[height+1][width+1].color == self.placement[height+2][width+2].color == self.placement[height+3][width+3].color == "gold2"):
                    info.text.config(text="Yellow Wins!")
                    self.perm = False
                    break
                width += 1
            height += 1
                    
    def Diagonal2(self): #checks for diagonal left wins 
        height = 0
        while(height < 3):#checks for the same value going up  and to the left once
            width = len(self.placement[height])-1
            while(width > len(self.placement)-4):
                if(self.placement[height][width].color == self.placement[height+1][width-1].color == self.placement[height+2][width-2].color == self.placement[height+3][width-3].color == "firebrick3"):
                    info.text.config(text="Red Wins!")
                    self.perm = False
                    break
                elif(self.placement[height][width].color == self.placement[height+1][width-1].color == self.placement[height+2][width-2].color == self.placement[height+3][width-3].color == "gold2"):
                    info.text.config(text="Yellow Wins!")
                    self.perm = False
                    break
                width -= 1
            height += 1

root = Tk()
root.geometry("500x550")
root.title("Connect 4 TKINTER")

info = Info(root)
info.grid(row=0, column=0)

text = Board(root)
text.grid(row=1, column=0)

def restart(): #restarts the game
    global info
    info.text.config(text="")
    
    info = Info(root)
    info.grid(row=0, column=0)

    text = Board(root)
    text.grid(row=1, column=0)

Button(root, text="Restart", command=restart).grid(row=2, column=0, pady=30)

root.mainloop()
