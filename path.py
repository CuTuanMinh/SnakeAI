import sys
import random
import copy
from PIL import Image,ImageTk
from tkinter import Tk,Frame,Canvas,ALL,NW,Menu

def next_node(x,y):
	nextnode=[]
	if ((x==0) & (y==0)):
		nextnode.append([x+10,y])
		nextnode.append([x,y+10])
	elif ((x==290) & (y==0)):
		nextnode.append([x-10,y])
		nextnode.append([x,y+10])
	elif ((x==0) & (y==290)):
		nextnode.append([x,y-10])
		nextnode.append([x+10,y])
	elif ((x==290) & (y==290)):
		nextnode.append([x,y-10])
		nextnode.append([x-10,y])
	elif ((y==0) & (x>0) & (x<290)):
		nextnode.append([x+10,y])
		nextnode.append([x-10,y])
		nextnode.append([x,y+10])
	elif ((x==0) & (y>0) & (y<290)):
		nextnode.append([x,y-10])
		nextnode.append([x,y+10])
		nextnode.append([x+10,y])
	elif ((y==290) & (x>0) & (x<290)):
		nextnode.append([x+10,y])
		nextnode.append([x-10,y])
		nextnode.append([x,y-10])
	elif ((x==290) & (y>0) & (y<290)):
		nextnode.append([x,y-10])
		nextnode.append([x,y+10])
		nextnode.append([x-10,y])
	else:
		nextnode.append([x,y+10])
		nextnode.append([x,y-10])
		nextnode.append([x-10,y])
		nextnode.append([x+10,y])
	return nextnode

def yes(a,b):
	n=next_node(a[0],a[1])
	if b in n: return True
	else: return False

def findPath(tick):
	ope=[]
	close=[]
	tic=[]
	for i in tick:
		ix=int(i[0])
		iy=int(i[1])
		tic.append([ix,iy])

	node_apple=tic.pop(0)
	present=tic.pop(0)

	while (present!=node_apple):
		close.append(present)
		nex=next_node(present[0],present[1])
		for j in nex:
			if ((j not in tic) & (j not in close) & (j not in ope)):
				ope.append(j)
		present=ope.pop(0)
			# if ope==[]: break

	close.append(node_apple)

	close.reverse()
	heada=close.pop(0)
	close3=[]
	close3.append(heada)
	headb=close3[len(close3)-1]

	for i in close:
		if yes(i,headb)==True:
			close3.append(i)
			headb=close3[len(close3)-1]
	close3.reverse()
	turn=[]
		
	for i in range(0,len(close3)-1):
		if ((close3[i+1][0]==close3[i][0]) & (close3[i+1][1]>close3[i][1])):
			turn.append(3)
		if ((close3[i+1][0]==close3[i][0]) & (close3[i+1][1]<close3[i][1])):
			turn.append(2)
		if ((close3[i+1][0]>close3[i][0]) & (close3[i+1][1]==close3[i][1])):
			turn.append(1)
		if ((close3[i+1][0]<close3[i][0]) & (close3[i+1][1]==close3[i][1])):
			turn.append(0)

	return turn

		