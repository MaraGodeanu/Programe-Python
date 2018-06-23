import pygame
import sys

pygame.init()

running=True
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Mario's World")
clock=pygame.time.Clock()

PINK=(220,40,166)
walking=[pygame.transform.scale(pygame.image.load("images/mario/mario2.png").convert_alpha(),(32,64)), 
         pygame.transform.scale(pygame.image.load("images/mario/mario3.png").convert_alpha(),(32,64)),
         pygame.transform.scale(pygame.image.load("images/mario/mario4.png").convert_alpha(),(32,64))]
mariox=500
marioy=500
imagemario=0
direction=0

while running:
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
            mariox=mariox + 10
            imagemario=(imagemario+1)%3
            direction=0
            
    if keys[pygame.K_LEFT]:
            mariox=mariox - 10
            imagemario=(imagemario - 1)%3
            direction=1
            
            
            
    screen.fill(PINK)
    
    if direction==1:
        screen.blit(pygame.transform.flip(walking[imagemario],True,False),(mariox,marioy))
        
    else:
        
        screen.blit(walking[imagemario],(mariox,marioy))
   
    pygame.display.flip()        
    clock.tick(25)        
    
pygame.quit()
sys.exit()    
            