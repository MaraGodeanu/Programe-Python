import pygame
import sys
import math
import time
import random

def dreptunghi(screen, x, y, l, w, color):
    pygame.draw.line(screen, color, [x, y], [x + l, y])
    pygame.draw.line(screen, color, [x+ l,y], [x + l,y + w])
    pygame.draw.line(screen, color, [x + l,y + w], [x ,y + w])
    pygame.draw.line(screen, color, [x ,y + w],[x ,y ])
    
def paleta(screen, X, Y, L, W,color):
    pygame.draw.line(screen, color, [X, Y], [X + L, Y])
    pygame.draw.line(screen, color, [X + L,Y],[X +L,Y+ W])
    pygame.draw.line(screen, color, [X + L,Y + W], [X,Y + W])
    pygame.draw.line(screen, color, [X,Y + W],[X,Y])
    
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

#culorile sunt RED,GREEN,BLUE    
RED = (255 ,0, 0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)
pygame.init()

score=0

size=[500, 350]
screen=pygame.display.set_mode(size)

px=200
py=280

r=7

mx=250
my=50

#ui=random.randint(0,360)* math.pi/180
ui=0

pdir=0

cycle=0

keypush= -1

caramizi=[1,1,1,1,1,1,1,1,1]

won=False
lose=False

lives=3
textcount=0

pygame.display.set_caption("PRO-LEVEL BREAK-OUT")
font=pygame.font.SysFont('Calibri',25,True,False)


mdir=2
done=False
clock=pygame.time.Clock()

pygame.key.set_repeat(1,10)

while not done: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            px=px + 5
            if pdir<0:
                pdir=0
            pdir=pdir + 1
            if pdir>5:
                pdir=5
            keypush=cycle
            if px+100>=500:
                px=400
    
        if keys[pygame.K_LEFT]: 
            px=px - 5
            if pdir>0:
                pdir=0
            pdir=pdir - 1
            if pdir<-5:
                pdir=-5
            keypush=cycle
            if px<=0:
                px=0
                
            
        if abs(keypush-cycle) >15:
            pdir=0
            
                
                
    screen.fill(WHITE)
    dreptunghi(screen,0,300,500,5,BLACK)
    textscore= font.render("score: " + str(score),True,BLACK)
    screen.blit(textscore,[225,325])
    textlives= font.render("lives: "+ str(lives),True,BLACK)
    screen.blit(textlives,[10,325])
    
    
    
    if score==90:
        wintext=font.render("YOU WIN! ;)",True,GREEN)
        screen.blit(wintext,[225,175])    
        done=True
        won=True
        
    if lives==0:
        losetext=font.render("YOU LOSE! :(",True,RED)
        screen.blit(losetext,[225,175])
        done=True
        lose=True
        
    if my + r >= 300 :
        lives=lives-1
        textcount=200
        
    if textcount>0:
        textcount=textcount-1     
        textliveslost=font.render("- 1 LIFE",True,BLACK)
        screen.blit(textliveslost,[400,325])
        mx=250
        my=50
        
    for i in range(9):
        if caramizi[i]==1:
            dreptunghi(screen, 25 + i*50, 10, 50, 25, RED)
    
    paleta(screen, px, py,100,10,BLUE)
    
    mx=mx + mdir * math.sin(ui) 
    if mx <= 0 + r:
        ui= - ui
        
    if mx>= 500 - r:
        ui= - ui
    my=my + mdir * math.cos(ui) 
    
    if my <= 0 + r:
        ui= math.pi - ui
        
        #AICI E PALETA
    if intersects(mx, my, r, px,py,px+ 100,py+10) : 
       # if pdir!=0:
           # ui=math.pi -ui + pdir * math.pi/16
        #else:
           # ui=math.pi -ui
        #ui=math.pi - math.atan2(my,mx) 
        #ui=math.pi/2 + math.atan2(my,mx)
        #ui=3*math.pi/2 - math.atan2(my,mx)
        if px <= mx <= px + 50:
            ui= 3*math.pi/2 - math.atan2(my,mx)
        else:
            ui=math.pi/2 + math.atan2(my,mx)
        

        
    if my>= 300 - r :   
        ui= math.pi -ui
  # AICI E CARAMIDA  
    for i in range(9):
        
        #if caramizi[i]==1 and (10 +25+r -2<=int(my)<=10 + 25 + r+2) and (25 + i*50<=mx<=25 + i*50 + 50)  :
            #caramizi[i]=0
            #score=score+10
            #ui=math.pi - ui
        if caramizi[i]==1 and intersects(mx,my,r,25+i*50,10,25+i*50+50,25):
            caramizi[i]=0
            score=score+10
            ui=math.pi - math.atan2(my,mx)
        if caramizi[i]==1 and (10-2<=my <= 10 +25+2) and  (mx + r-2<=25+i*50<=mx+r+2):
            caramizi[i]=0
            ui= -ui
            score=score+10
        if caramizi[i]==1 and (10-2<=my <= 10 +25+2) and  (mx + r-2<=25+50+i*50<=mx+r+2):
            caramizi[i]=0
            ui= -ui
            score=score+10
        
    minge(screen,int(mx),int(my), r,GREEN, 0)
     
    pygame.display.flip()
    
    clock.tick(100)
    cycle=cycle + 1
    cycle=cycle %60 
    
if won:
    time.sleep(5)
if lose:
    time.sleep(5)
    
pygame.quit()
sys.exit()    