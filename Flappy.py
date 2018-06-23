import random

alien = Actor('alien')
alien.pos = 240, 240
walls=[]
alive=True    
score=0    


WIDTH = 480
HEIGHT = alien.height + 520



#def update():
#    alien.left += 2
#    if alien.left > WIDTH:
#       alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
        

    

def update():
    global score,alive
    if keyboard.left:
        alien.x -= 1
    elif keyboard.right:
        alien.x += 1

    if keyboard.UP:
        alien.y -=2
    elif keyboard.DOWN:
        alien.y += 2
    if alien.collidelist(walls) != -1:
        alive=False
    else:    
        score=score+1    
    
    
def addwall():
    topwallheight=random.randint(10,400)
    bottomwallheight=random.randint(topwallheight+120,HEIGHT)


    topwall=Actor('flappy,wall2',pos=(530,topwallheight),anchor=("center","bottom"))
    bottomwall=Actor('flappy,wall2',pos=(530,bottomwallheight),anchor=("center","top"))

    topwall.animation=animate(topwall,pos=(-50,topwall.y),duration=5)
    bottomwall.animation=animate(bottomwall,pos=(-50,bottomwall.y),duration=5)
    walls.extend([topwall,bottomwall])    



def draw():
    global alive
    if alive:
        screen.clear()
        screen.fill((0,51,102))
        alien.draw()    
        screen.draw.text(str(score),(20,500))
        
        for i in walls:
            i.draw()
    else:
        screen.draw.text("GAME OVER!",(240,300))
        
addwall()        
clock.schedule_interval(addwall,3)    