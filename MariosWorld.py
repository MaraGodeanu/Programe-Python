import pygame
import sys

pygame.init()

running=True
screen = pygame.display.set_mode((1000,595))
pygame.display.set_caption("Mario's World")
clock=pygame.time.Clock()


##########IMAGES


PINK=(220,40,166)
jumping=pygame.transform.scale(pygame.image.load("images/mario/mario6.png").convert_alpha(),(32,64))
standing=pygame.transform.scale(pygame.image.load("images/mario/mario1.png").convert_alpha(),(32,64))
walking=[pygame.transform.scale(pygame.image.load("images/mario/mario2.png").convert_alpha(),(32,64)), 
         pygame.transform.scale(pygame.image.load("images/mario/mario3.png").convert_alpha(),(32,64)),
         pygame.transform.scale(pygame.image.load("images/mario/mario4.png").convert_alpha(),(32,64))]
poleing=pygame.transform.scale(pygame.image.load("images/mario/mario9.png").convert_alpha(),(32,64))
floor=pygame.transform.scale(pygame.image.load("images/floor.png").convert_alpha(),(30,32))
platform=pygame.transform.scale(pygame.image.load("images/platform.png").convert_alpha(),(64,30))
poletop=pygame.image.load("images/mario/pole_top.png").convert_alpha()
pole=pygame.transform.scale(pygame.image.load("images/mario/pole.png").convert_alpha(),(4,32))

#########PLATFORMS

platforms=[(700,450),(764,450),(300,420),(364,420),(200,350),(264,350),(830,490),(0,490)]
poles=[(600,250+64)]


##########VARIABLES


mariox=500
marioy=500
imagemario=0
direction=0
moving=False
flying=False
falling=False
sliding=False
jumpcounter=0
poletouch=None



############DO NOT ERASE/VITAL STUFF

while running:
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
######### KEYS            
            
    keys = pygame.key.get_pressed()
    
    
    
    
    
    if keys[pygame.K_RIGHT]:
        willcollide=False
        
        for p in platforms:
             if pygame.Rect((mariox+10,marioy),(32,64)).colliderect(pygame.Rect(p,(64,30))):
                 willcollide=True
                 mariox=p[0]-33
                 break
        if not willcollide: 
            mariox=mariox + 10
            imagemario=(imagemario+1)%3
            direction=0
            moving=True
        willcollide=False 
        for p in poles:
            if pygame.Rect((mariox,marioy),(32,64)).colliderect(pygame.Rect(p,(4,250+64))):
                 willcollide=True
                 if sliding :
                     mariox=p[0]+5
                     poletouch="left"
                 else:
                     sliding=True
                     mariox=p[0]-33
                 break
        if poletouch=="left" and not willcollide:
             print("problem93")            
             sliding=False
             poletouch=None
           
        
            
    elif keys[pygame.K_LEFT]:
        willcollide=False
        for p in platforms:
             if pygame.Rect((mariox-10,marioy),(32,64)).colliderect(pygame.Rect(p,(64,30))):
                 willcollide=True
                 mariox=p[0]+65
                 break
        if not willcollide: 
            mariox=mariox - 10
            imagemario=(imagemario-1)%3
            direction=1
            moving=True
        willcollide=False 
        for p in poles:
            if pygame.Rect((mariox,marioy),(32,64)).colliderect(pygame.Rect(p,(4,250+64))):
                 print("touching")
                 willcollide=True
                 if sliding :
                     print("moving left")
                     mariox=p[0]-33
                     poletouch="right"
                 else:
                     print("will slide")
                     sliding=True
                     mariox=p[0]+5
                 break
        if poletouch=="right" and not willcollide:
            print("problem126")
            sliding=False
            poletouch=None
            
    if keys[pygame.K_DOWN]:
        willcollide=False        
        if sliding:
            print("is sliding")
            for p in platforms:
                if pygame.Rect((mariox,marioy+10),(32,64)).colliderect(pygame.Rect(p,(64,30))):
                    willcollide=True
                    platformheight=p[1]
                    break
            if not willcollide and marioy<=490:
                marioy+=10
            elif willcollide:
                marioy=platformheight-65
                
         
            
    if keys[pygame.K_UP]:
        willcollide=False
        if not falling:
            if jumpcounter<=7 and not sliding:
                
                for p in platforms:
                    if (pygame.Rect((mariox,marioy-20),(32,64)).colliderect(pygame.Rect(p,(64,30))) and marioy>=p[1]):
                        willcollide=True
                        falling=True
                        platformheight=p[1]
                        break
                if not willcollide:
                    marioy=marioy - 20
                    flying=True
                    jumpcounter += 1
                else:
                    if platformheight+30<500:
                        marioy=platformheight+30
            elif marioy<=500 and not sliding:
                falling=True
        if sliding:
                print("is sliding")
                for p in poles:
                   if pygame.Rect((mariox,marioy-10),(32,64)).colliderect(pygame.Rect((p[0]-2,p[1]-8),(8,8))):
                         willcollide=True
                         platformheight=p[1]-8
                         break
                   if not willcollide:
                         marioy -=10
                
                
    else:
        if marioy<=500:
            falling=True
        
########MOVEMENT OR NOT
        
    if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
            moving=False
#########ON THE FLOOR       
    if marioy>=500:
            
            flying=False
            falling=False
            jumpcounter=0
            
   
###########SOME COLLISION AND FALLING

     
    if marioy<500:
        willcollide=False
        if falling and not sliding:
            marioy= marioy +10           
            platformheight=500
            for p in platforms :
                if  (pygame.Rect((mariox,marioy),(32,64)).colliderect(pygame.Rect(p,(64,30))) and marioy<=p[1]):
                    willcollide=True
                    platformheight=p[1]
                    marioy=platformheight-64
                    break
                
                     
                     
            if willcollide and marioy<=platformheight:  
                falling=False
                flying=False
                
                jumpcounter=0
                
                
                
    else:
        
        falling=False        
        jumpcounter=0
        
        
  #########POSES and MOVEMENTSTATE            
            
    screen.fill(PINK)
    if moving and not flying:
        if direction==1:
            screen.blit(pygame.transform.flip(walking[imagemario],True,False),(mariox,marioy))     
        else:
            screen.blit(walking[imagemario],(mariox,marioy))
            
    elif moving and flying :
         if sliding:
             sprite=poleing
         else:
             sprite=jumping
        
        
         if direction==1:
             screen.blit(pygame.transform.flip(sprite,True,False),(mariox,marioy))
         
         else:   
             screen.blit(sprite,(mariox,marioy))
             
             
    elif flying:
        if sliding:
            if poletouch=="right":
                sprite=poleing
            else:
                sprite=pygame.transform.flip(poleing,True,False)
        else:
             sprite=jumping
        screen.blit(sprite,(mariox,marioy))    
        
        
    else:
        screen.blit(standing,(mariox,marioy))
      
        
    for i in range(34):
        screen.blit(floor,(i*30,564))
        
    for p in platforms:    
        screen.blit(platform,p)    
    
    for p in poles:
        screen.blit(pygame.transform.scale(pole,(4,250)),p)
        screen.blit(poletop,(p[0]-2,p[1]-8))
        
    pygame.display.flip()        
    clock.tick(25)        
    
pygame.quit()
sys.exit()    
            