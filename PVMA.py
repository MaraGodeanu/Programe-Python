# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 10:48:30 2018

@author: Administrator
"""
import pygame
import sys

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1366,768))
#pygame.display.flip
#############Episode 1,Cutscene 1 #################################3
dbox=pygame.image.load("images\DialogueBox.png").convert()
E1C1I1=pygame.image.load("images\E1C1I1.png").convert()
E1C1I2=pygame.image.load("images\E1C1I2.png").convert()
E1C1I3=pygame.image.load("images\E1C1I3.png").convert()
E1C1I4=pygame.image.load("images\E1C1I4.png").convert()
E1C1I5=pygame.image.load("images\E1C1I5.png").convert()
E1C1I6=pygame.image.load("images\E1C1I6.png").convert()


PINK=(220,40,166)

start_time = pygame.time.get_ticks()
clock=pygame.time.Clock()
#DISPLAYSURF.fill(PINK)

running=True
while running:
    if pygame.time.get_ticks()<start_time+5000:
        DISPLAYSURF.blit(E1C1I1,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))
    if 5000<=pygame.time.get_ticks()<start_time+10000:    
        DISPLAYSURF.blit(E1C1I2,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))
    if 10000<=pygame.time.get_ticks()<start_time +15000:    
        DISPLAYSURF.blit(E1C1I3,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))
    if 15000<=pygame.time.get_ticks()<start_time +20000:
        DISPLAYSURF.blit(E1C1I4,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))
    if 20000<=pygame.time.get_ticks()<start_time +25000:
        DISPLAYSURF.blit(E1C1I5,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))
    if 25000<=pygame.time.get_ticks()<start_time +30000:
        DISPLAYSURF.blit(E1C1I6,(0,0))
        DISPLAYSURF.blit(dbox,(368,550))     
    if pygame.time.get_ticks()>=30000:
        DISPLAYSURF.fill(PINK)
    
    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            running = False
            
        if keys[pygame.K_ESCAPE]:
            running = False
            
              
            
            
            
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
sys.exit()    