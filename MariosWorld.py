import pygame
import sys

pygame.init()

running=True
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Mario's World")
clock=pygame.time.Clock()

PINK=(220,40,166)
jumping=pygame.transform.scale(pygame.image.load("images/mario/mario6.png").convert_alpha(),(32,64))
standing=pygame.transform.scale(pygame.image.load("images/mario/mario1.png").convert_alpha(),(32,64))
walking=[pygame.transform.scale(pygame.image.load("images/mario/mario2.png").convert_alpha(),(32,64)), 
         pygame.transform.scale(pygame.image.load("images/mario/mario3.png").convert_alpha(),(32,64)),
         pygame.transform.scale(pygame.image.load("images/mario/mario4.png").convert_alpha(),(32,64))]
mariox=500
marioy=500
imagemario=0
direction=0
moving=False
flying=False

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
            flying=False
            
    elif keys[pygame.K_LEFT]:
            mariox=mariox - 10
            imagemario=(imagemario - 1)%3
            direction=1
            moving=True
            flying=False
            
    elif keys[pygame.K_UP]:
            marioy=marioy - 20
            flying=True
            
    else:
            moving=False     
            
            if marioy>=500:    
                flying=False
            
            
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
        if marioy<500:
            marioy=marioy+10
        
        
    else:
        if marioy<500:
            marioy=marioy+10
            
        screen.blit(standing,(mariox,marioy))
    pygame.display.flip()        
    clock.tick(25)        
    
pygame.quit()
sys.exit()    
            