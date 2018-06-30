import pygame
import sys

pygame.init()

running=True
screen = pygame.display.set_mode((1000,595))
pygame.display.set_caption("Mario's World")
clock=pygame.time.Clock()

PINK=(220,40,166)
jumping=pygame.transform.scale(pygame.image.load("images/mario/mario6.png").convert_alpha(),(32,64))
standing=pygame.transform.scale(pygame.image.load("images/mario/mario1.png").convert_alpha(),(32,64))
walking=[pygame.transform.scale(pygame.image.load("images/mario/mario2.png").convert_alpha(),(32,64)), 
         pygame.transform.scale(pygame.image.load("images/mario/mario3.png").convert_alpha(),(32,64)),
         pygame.transform.scale(pygame.image.load("images/mario/mario4.png").convert_alpha(),(32,64))]
floor=pygame.transform.scale(pygame.image.load("images/floor.png").convert_alpha(),(30,32))
platform=pygame.transform.scale(pygame.image.load("images/platform.png").convert_alpha(),(64,30))


platforms=[(700,450),(764,450),(300,420),(364,420),(200,350),(264,350)]



mariox=500
marioy=500
imagemario=0
direction=0
moving=False
flying=False
falling=False
jumpcounter=0


while running:
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        
            
    keys = pygame.key.get_pressed()
    
    
    
    
    
    if keys[pygame.K_RIGHT]:
            mariox=mariox + 10
            imagemario=(imagemario+1)%3
            direction=0
            moving=True
            
            
    elif keys[pygame.K_LEFT]:
            mariox=mariox - 10
            imagemario=(imagemario - 1)%3
            direction=1
            moving=True
            
            
    if keys[pygame.K_UP]:
        if not falling:
            if jumpcounter<=7:
                marioy=marioy - 20
                flying=True
                jumpcounter += 1
            elif marioy<=500:
                falling=True
    else:
        if marioy<=500:
            falling=True
        
        
    if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
            moving=False
        
    if marioy>=500:    
            flying=False
            falling=False
            jumpcounter=0
            
    screen.fill(PINK)
    if moving and not flying:
        if direction==1:
            screen.blit(pygame.transform.flip(walking[imagemario],True,False),(mariox,marioy))     
        else:
            screen.blit(walking[imagemario],(mariox,marioy))
            
    elif moving and flying :
         if direction==1:
             screen.blit(pygame.transform.flip(jumping,True,False),(mariox,marioy))
         
         else:   
             screen.blit(jumping,(mariox,marioy))
             
             
    elif flying:
        screen.blit(jumping,(mariox,marioy))    
        
        
    else:
        screen.blit(standing,(mariox,marioy))
        
    if marioy<500:
        if falling:
            willcollide=False
            platformheight=500
            for p in platforms :
                if  (pygame.Rect((mariox,marioy),(32,64)).colliderect(pygame.Rect(p,(64,30))) and marioy<=p[1]):
                    willcollide=True
                    platformheight=p[1]
                    break
                    
            if not willcollide:        
                marioy=marioy+10
            elif marioy<=platformheight:
                falling=False
                jumpcounter=0
    else:
        falling=False        
        jumpcounter=0
        
    for i in range(34):
        screen.blit(floor,(i*30,564))
        
    for p in platforms:    
        screen.blit(platform,p)    
          
        
    pygame.display.flip()        
    clock.tick(25)        
    
pygame.quit()
sys.exit()    
            