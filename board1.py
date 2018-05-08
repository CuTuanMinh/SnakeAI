import sys
import random
import copy
import path
from PIL import Image,ImageTk
from tkinter import Tk,Frame,Canvas,ALL,NW,Menu


DELAY=100
DOT_SIZE=10
RAND_POS=29
WIDTH=300
HEIGHT=300

# road=[]

class Board(Canvas):
	def __init__(self,parent):
		Canvas.__init__(self,width=300,height=300,background="black",highlightthickness=0)
		self.parent=parent
		self.initGame()
		self.pack()
	
	def initGame(self):
		self.right=True
		self.left=False
		self.up=False
		self.down=False

		self.inGame=True
		self.score=0

		self.apple_x=100
		self.apple_y=190

		self.x0=50
		self.y0=50
		self.x1=40
		self.y1=50
		self.x2=30
		self.y2=50
		
			

		self.mapImage=Image.open("y2.jpeg")
		self.mapImage.thumbnail((10,10),Image.ANTIALIAS)
		self.map=ImageTk.PhotoImage(self.mapImage)

		self.dotplayerImage=Image.open("y5.jpg")
		self.dotplayerImage.thumbnail((10,10),Image.ANTIALIAS)
		self.dotplayer=ImageTk.PhotoImage(self.dotplayerImage)

		self.headImage=Image.open("y6.jpeg")
		self.headImage.thumbnail((10,10),Image.ANTIALIAS)
		self.head=ImageTk.PhotoImage(self.headImage)
		
		self.createObjects()
		self.createMap()
		self.locateApple()

		self.bind_all("<Key>",self.onKeyPressed)
		self.after(DELAY,self.onTimer)
	
	

	def createObjects(self):
		self.create_text(30,10,text="Score: {0}".format(self.score),tag="scorePlayer",fill="yellow")		
		self.create_image(self.apple_x,self.apple_y,image=self.head,anchor=NW,tag="apple")

		self.create_image(self.x0,self.y0,image=self.dotplayer,anchor=NW,tag="head")
		self.create_image(self.x1,self.y1,image=self.dotplayer,anchor=NW,tag="dot")
		self.create_image(self.x2,self.y2,image=self.dotplayer,anchor=NW,tag="dot")


	def createMap(self):
		tick1=[[self.apple_x,self.apple_y],[self.x0,self.y0],[self.x1,self.y1],[self.x2,self.y2]]
		tk=[]
		for i in range(20):
			r=random.randint(0,RAND_POS)
			a_x=float(r*DOT_SIZE)
			w=random.randint(0,RAND_POS)
			a_y=float(w*DOT_SIZE)
			if [a_x,a_y] not in tk:
				tk.append([a_x,a_y])
		for i in tk:
			if i not in tick1:		
				self.create_image(i[0],i[1],image=self.map,anchor=NW,tag="map")

	def locateApple(self):
		tick2=[]
		apple=self.find_withtag("apple")
		self.delete(apple[0])

		maps=self.find_withtag("map")
		head=self.find_withtag("head")
		dots=self.find_withtag("dot")

		headx,heady=self.coords(head)
		tick2.append([headx,heady])

		for dot in dots:
			dotx,doty=self.coords(dot)
			tick2.append([dotx,doty])

		for mep in maps:
			mepx,mepy=self.coords(mep)
			tick2.append([mepx,mepy])

		r=random.randint(0,RAND_POS)
		self.apple_x=float(r*DOT_SIZE)
		w=random.randint(0,RAND_POS)
		self.apple_y=float(w*DOT_SIZE)

		while ([self.apple_x,self.apple_y] in tick2):
			r=random.randint(0,RAND_POS)
			self.apple_x=float(r*DOT_SIZE)
			w=random.randint(0,RAND_POS)
			self.apple_y=float(w*DOT_SIZE)

		self.create_image(self.apple_x,self.apple_y,image=self.head,anchor=NW,tag="apple")

		
	def checkCollisions(self):
		tick=[]
		
		meps=self.find_withtag("map")
		for mep in meps:
			mepx,mepy=self.coords(mep)
			tick.append([mepx,mepy])

		dots=self.find_withtag("dot")
		for dot in dots:
			dotx,doty=self.coords(dot)
			tick.append([dotx,doty])

		head=self.find_withtag("head")
		headx,heady=self.coords(head)

		if [headx,heady] in tick:
			self.inGame=False
		if headx<0:
			self.inGame=False
		if headx>300:
			self.inGame=False
		if heady<0:
			self.inGame=False
		if heady>300:
			self.inGame=False


	def CheckApple(self):
		apple=self.find_withtag("apple")
		applex,appley=self.coords(apple)

		head=self.find_withtag("head")
		headx,heady=self.coords(head)

		if ((applex==headx) & (appley==heady)):
			self.score+=1
			self.create_image(applex,appley,image=self.dotplayer,anchor=NW,tag="dot")
			self.locateApple()
			self.drawScorePlayer()
			
	def gameOver(self):
		# self.delete(ALL)
		# self.create_text(self.winfo_width()/2,self.winfo_height()/2,text="Game Over with score {0}".format(self.score),fill="white")
		self.create_text(self.winfo_width()/2,self.winfo_height()/2,text="Game Over",fill="white")


	def doMove(self):
		dots=self.find_withtag("dot")
		head=self.find_withtag("head")
		item=dots+head
		z=0
		while z<len(item)-1:
			c1=self.coords(item[z])
			c2=self.coords(item[z+1])
			self.move(item[z],c2[0]-c1[0],c2[1]-c1[1])
			z+=1
		if self.left:
				self.move(head,-10,0)
		if self.right:
				self.move(head,10,0)
		if self.up:
				self.move(head,0,-10)
		if self.down:
				self.move(head,0,10)



	def onKeyPressed(self,e):
		key=e.keysym
		if key=="Left" and not self.right:
			self.left=True
			self.up=False
			self.down=False

		if key=="Right" and not self.left:
			self.right=True
			self.up=False
			self.down=False

		if key=="Up" and not self.down:
			self.up=True
			self.right=False
			self.left=False

		if key=="Down" and not self.up:
			self.down=True
			self.right=False
			self.left=False

	def onTimer(self):
		if self.inGame:
			self.checkCollisions()
			self.CheckApple()
			self.doMove()
			self.after(DELAY,self.onTimer)
		else:
			self.gameOver()

	def drawScorePlayer(self):
		scorePlayer=self.find_withtag("scorePlayer")
		self.itemconfigure(scorePlayer,text="Score: {0}".format(self.score))







