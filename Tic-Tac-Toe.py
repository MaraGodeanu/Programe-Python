import pygame
import random

WIDTH=400
HEIGHT=400


def grid(x,y,l,w,color):
    screen.draw.line([x,y],[x+l,y],color)
    screen.draw.line([x, 85+y+y/3],[x+l,85+y+y/3],color)
    screen.draw.line([x,125+2*y+2*y/3],[x+l,125+2*y+2*y/3],color)
    screen.draw.line([x,y+w],[x+l,y+w],color)
    screen.draw.line([x,y],[x,y+w],color)
    screen.draw.line([x+l/3,y],[x+l/3,y+w],color)
    screen.draw.line([x+2*l/3,y],[x+2*l/3,y+w],color)    
    screen.draw.line([x+l,y],[x+l,y+w],color)
    


BLACK=(0,0,0)
X=Actor('x-tictactoe2')
gx=50
gy=50
G=[[None,None,None],[None,None,None],[None,None,None]]
nextsign=0
ongoing=True
winningplayer=None
fps=0

O=Actor('o-tictactoe1')

def on_mouse_down(pos):
    global nextsign,ongoing,winningplayer
    row=None
    col=None
    if 50<=pos[0]<150:
        col=0
        x=100
    elif 150<pos[0]<250:    
        col=1
        x=200
    elif 250<pos[0]<=350:
        col=2
        x=300
    if 50<pos[1]<150:
        row=0
        y=100
    elif 150<pos[1]<250:
        row=1
        y=200
    elif 250<pos[1]<=350:    
        row=2
        y=300
    if col in [0,1,2] and row in [0,1,2] and not G[row][col]:
        if nextsign==0:
            G[row][col]=(Actor('x-tictactoe2'),"x")
            G[row][col][0].pos=(x,y)
            nextsign=1
        #else:
        #    G[col][row]=(Actor('o-tictactoe1'),"o")
        #    G[col][row][0].pos=(x,y)
        #    nextsign=0
        
def computermove(row,col):
   global nextsign
   if nextsign==1:
       G[row][col]=(Actor('o-tictactoe1'),"o")
       G[row][col][0].pos=((col+1)*100,(row+1)*100)
       nextsign=0         
       print(row,col)     
        
def computermovelinear():
    global nextsign
    for row in range (3):
        for col in range (3):
            if not G[row][col] and nextsign==1:
                computermove(row,col)
                 
                
                
def computermoverandom():
   global nextsign
   emptycells=[]
   for row in range (3):
       for col in range (3):
           if not G[row][col] and nextsign==1:
               emptycells.append((row,col))
   if len(emptycells)==1:
        row,col=emptycells[0]
   elif len(emptycells)>1:
        
       row,col=emptycells[random.randint(0,len(emptycells)-1)]
       computermove(row,col)


def computermovesmarter():
    global nextsign
    for i in range (3):
        #print(G[i][0][1],G[i][1][1])
        if G[i][0] and G[i][1] and G[i][0][1]==G[i][1][1] and not G[i][2]:
            computermove(i,2)
        if G[i][1] and G[i][2] and G[i][1][1]==G[i][2][1] and not G[i][0]:
            computermove(i,0)
        if G[i][0] and G[i][2] and G[i][0][1]==G[i][2][1] and not G[i][1]:
            computermove(i,1)
            
        if G[0][i] and G[1][i] and G[0][i][1]==G[1][i][1] and not G[2][i]:
            computermove(2,i)
        if G[1][i] and G[2][i] and G[1][i][1]==G[2][i][1] and not G[0][i]:
            computermove(0,i)
        if G[0][i] and G[2][i] and G[0][i][1]==G[2][i][1] and not G[1][i]:
            computermove(1,i)
            
    if G[0][0] and G[1][1] and G[0][0][1]==G[1][1][1] and not G[2][2]:
        computermove(2,2)
    if G[2][2] and G[1][1] and G[2][2][1]==G[1][1][1] and not G[0][0]:
        computermove(0,0)
    if G[0][0] and G[2][2] and G[0][0][1]==G[2][2][1] and not G[1][1]:
        computermove(1,1)
        
    if G[0][2] and G[1][1] and G[0][2][1]==G[1][1][1] and not G[2][0]:
        computermove(2,0)
    if G[2][0] and G[1][1] and G[2][0][1]==G[1][1][1] and not G[0][2]:
        computermove(0,2)
    if G[0][2] and G[2][0] and G[0][2][1]==G[2][0][1] and not G[1][1]:
        computermove(1,1)                             
            
    if nextsign==1:
        computermoverandom()
        
        
def update():
    global nextsign,ongoing,winningplayer,fps
    fps+=1
    if nextsign==1:
        computermovesmarter()       
                      
    for row in G:
            if row[0] and row[1] and row[2] and row[0][1]==row[1][1]==row[2][1]:
                winningplayer=row[0][1]
                ongoing=False
    for col in range(3):
            if G[0][col] and G[1][col] and G[2][col] and G[0][col][1]==G[1][col][1]==G[2][col][1]:
                winningplayer=G[0][col][1]
                ongoing=False
    if G[0][0] and G[1][1] and G[2][2] and G[0][0][1]==G[1][1][1]==G[2][2][1]:
                winningplayer=G[2][2][1]
                ongoing=False
                
    if G[0][2] and G[1][1] and G[2][0] and G[0][2][1]==G[1][1][1]==G[2][0][1]:
                winningplayer=G[0][2][1]
                ongoing=False      
    if all([cell for row in G for cell in row]):
        ongoing=False
        
def draw():
    
    if ongoing:
                
        screen.clear()
        screen.fill((255,255,255))
        grid( gx, gy,300,300,BLACK)
        for row in G:
            for actor in row:
                if actor:
                    actor[0].draw()
        screen.draw.text(str(fps),(0,0),color="red")
    else:
        screen.clear()
        if winningplayer:           
            screen.draw.text("Player "+winningplayer+ " won!",(150,200))
        else:
            screen.draw.text("Draw",(175,200))