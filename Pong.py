import pygame
import sys
import math
import time
import random

#TASTELE SUNT K;M si A;Z

def linie(screen, x, y, l,color):
    pygame.draw.line(screen, color, [x, y],[x+1 , y+l])
    
    
def dreptunghi(screen, x, y, l, w, color):
    pygame.draw.line(screen, color, [x, y], [x + l, y])
    pygame.draw.line(screen, color, [x+ l,y], [x + l,y + w])
    pygame.draw.line(screen, color, [x + l,y + w], [x ,y + w])
    pygame.draw.line(screen, color, [x ,y + w],[x ,y ])
    
def minge(screen, x, y, r, color, w):
    pygame.draw.circle(screen, color,[x, y], r, w)    
    
def intersects(mx, my, r, left, top, right, bottom):
   if mx < left:
       closestX = left
   else:
       if mx > right:
           closestX = right
       else:
            closestX = mx

   if my < top:
       closestY = top
   else:
       if my > bottom:
           closestY = bottom
       else:
            closestY = my

   dx = closestX - mx
   dy = closestY - my

   return (dx * dx + dy * dy) <= r * r     
    
 #culori RED,GREEN,BLUE   
RED = (255 ,0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)

pygame.init()

size=[500, 350]
screen=pygame.display.set_mode(size)

#MINGE

r=7
my=50
mx=250
mdir=2
ui=random.randint(0,360)* math.pi/180

scoreS=0
scoreR=0

pygame.display.set_caption("PONG ")
font=pygame.font.SysFont('Calibri',25,True,False)

won=False

sx=5
rx=475
sy=125
ry=125
sdir=0
rdir=0
done=False
clock=pygame.time.Clock()

pygame.key.set_repeat(1,10)

while not done: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            if sy>2:
                sy-=2
             
        if keys[pygame.K_z]:
            if sy<249:
                sy+=2
            
        if keys[pygame.K_k]:
            if ry>2:
                ry-=2
            
        if keys[pygame.K_m]:
            if ry<249:
                ry+=2
                
    
    
            
    screen.fill(WHITE)
    
    dreptunghi(screen,5,sy,20,100,BLACK)
    
    textscoreR= font.render("score: " + str(scoreR),True,BLACK)
    screen.blit(textscoreR,[350,325])
    textscoreS= font.render("score: "+ str(scoreS),True,BLACK)
    screen.blit(textscoreS,[87,325])
    
    if scoreS==5:
        wintextS=font.render("PLAYER1 WINS! ",True,GREEN)
        screen.blit(wintextS,[225,175])    
        done=True
        won=True
    
    if scoreR==5:
        wintextR=font.render("PLAYER2 WINS !",True,GREEN)
        screen.blit(wintextR,[225,175])
        done=True
        won=True
    
    
    
    
    linie(screen,250,0,350,BLACK)
    dreptunghi(screen,475,ry,20,100,BLACK)
    minge(screen,int(mx),int(my),r,BLUE,0)
     
    if mx -r <=0:
        scoreR=scoreR+1
        mx=250
        my=50
    
    if mx + r>=500:
        scoreS=scoreS +1
        mx=250
        my=50
    
    mx=mx + mdir * math.sin(ui) 
    if mx <= 0 + r:
        ui= - ui
        
    if mx>= 500 - r:
        ui= - ui
    my=my + mdir * math.cos(ui) 
    
    if my <= 0 + r:
        ui= math.pi - ui                
                
    if my >= 350-r:
        ui=math.pi - ui
        
        
    if intersects(mx,my,r,sx,sy,sx+20,sy+100):
        ui= math.atan2(my,mx)
    
        
        
        
    if intersects(mx,my,r,rx,ry,rx+20,ry + 100):
        ui= - math.atan2(my,mx)
            
        
        
            

        
        print(scoreS,scoreR)
        
    pygame.display.flip()     
    clock.tick(100)
  
    if won:
        time.sleep(5)   
    
    
pygame.quit()
sys.exit()

