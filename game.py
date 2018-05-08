import sys
import random
import board1
import board2
from PIL import Image,ImageTk
from tkinter import Tk,Frame,Canvas,ALL,NW,Menu

class Snake(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.initUI()
	def initUI(self):
		self.parent.title("Snake")
		self.pack()
		menuBar=Menu(self.parent)
		self.parent.config(menu=menuBar)
		fileMenu1=Menu(menuBar)
		fileMenu1.add_command(label="Play",command=self.onBoard1)
		fileMenu1.add_command(label="New game",command=self.onBoard1Again)
		menuBar.add_cascade(label="Play 1",menu=fileMenu1)
		fileMenu2=Menu(menuBar)
		fileMenu2.add_command(label="Play",command=self.onBoard2)
		fileMenu2.add_command(label="New game",command=self.onBoard2Again)
		menuBar.add_cascade(label="Play 2",menu=fileMenu2)	
		menuBar.add_command(label="Quit",command=self.quit)	
	def onBoard1(self):
		global present1
		present1=board1.Board(self.parent)
	def onBoard1Again(self):
		global present1
		present1.destroy()
		present1=board1.Board(self.parent)
	def onBoard2(self):
		global present2
		present2=board2.Board(self.parent)
	def onBoard2Again(self):
		global present2
		present2.destroy()
		present2=board2.Board(self.parent)

root=Tk()
root.geometry("300x300+250+200")
Snake(root)
root.mainloop()