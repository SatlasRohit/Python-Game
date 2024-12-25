import pygame
import random
pygame.init()
#screen pixel size
screen=pygame.display.set_mode((829,631))
#game name
pygame.display.set_caption("Zig Zag Cars")
background=pygame.image.load("carBG.png")
playerx=415
playery=500
playerx_change=0
playery_change=0
x=0
#enemy images1 50,200,330,460,600,730
enemy1=pygame.image.load("enemycar1.png")
enemyx1=50
enemyy1=30
enemyx_change1=0
enemyy_change1=0
#enemy image2
enemy2=pygame.image.load("enemycar2.png")
enemyx2=200
enemyy2=-300
enemyx_change2=0
enemyy_change2=0
#enemy image3
enemy3=pygame.image.load("enemycar3.png")
enemyx3=330
enemyy3=-100
enemyx_change3=0
enemyy_change3=0
#enemy image4
enemy4=pygame.image.load("enemycar4.png")
enemyx4=600
enemyy4=-100
enemyx_change4=0
enemyy_change4=0
#enemy image5
enemy5=pygame.image.load("enemycar5.png")
enemyx5=730
enemyy5=-200
enemyx_change5=0
enemyy_change5=0
#player image 
player=pygame.image.load("car.png")
#player function
def playerfn(playerx,playery):
    screen.blit(player,(playerx,playery))
def enemya(x,y):
    screen.blit(enemy1,(x,y))
def enemyb(x,y):
    screen.blit(enemy2,(x,y))
def enemyc(x,y):
    screen.blit(enemy3,(x,y))
def enemyd(x,y):
    screen.blit(enemy4,(x,y))
def enemye(x,y):
    screen.blit(enemy5,(x,y))
num_of_enemies=5
running=True
#Infinite loop
while running:
    #screen background color code RGB-red,green,blue
    screen.fill((192,0,0))
    #screem background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                playery_change=-3
            elif event.key==pygame.K_DOWN:
                playery_change=3
            if event.key==pygame.K_RIGHT:
                playerx_change=3
            elif event.key==pygame.K_LEFT:
                playerx_change=-3
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playery_change=0
            elif event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                playerx_change=0
    #playery change
    playery+=playery_change
    #playerx change
    playerx+=playerx_change
    #player function call
    playerfn(playerx,playery)
    #player end movement
    if playerx>=709:
        playerx=709
    elif playerx<=0:
        playerx=0
    if playery>=511:
        playery=511
    elif playery<=0:
        playery=0
    #Enemy1 Movement
    if enemyy1<=631:
        x=0
        if x==0:
            enemyy_change1=2
        enemyy1+=enemyy_change1
        #enemy1 function call
        enemya(enemyx1,enemyy1)
    elif enemyy1>=631:
        x+=1
        if x>0:
            enemyy_change1=-200
        enemyy1=enemyy_change1
        #enemy1 function call
        enemya(enemyx1,enemyy1)
    #Enemy2 Movement
    if enemyy2<=631:
        x=0
        if x==0:
            enemyy_change2=2
        enemyy2+=enemyy_change2
        #enemy2 function call
        enemyb(enemyx2,enemyy2)
    elif enemyy2>=631:
        x+=1
        if x>0:
            enemyy_change2=-302
        enemyy2=enemyy_change2
        #enemy2 function call
        enemyb(enemyx2,enemyy2)
    #Enemy3 Movement
    if enemyy3<=631:
        x=0
        if x==0:
            enemyy_change3=2
        enemyy3+=enemyy_change3
        #enemy3 function call
        enemyc(enemyx3,enemyy3)
    elif enemyy3>=631:
        x+=1
        if x>0:
            enemyy_change3=-137
        enemyy3=enemyy_change3
        #enemy3 function call
        enemyc(enemyx3,enemyy3)
    #Enemy4 Movement
    if enemyy4<=631:
        x=0
        if x==0:
            enemyy_change4=2
        enemyy4+=enemyy_change4
        #enemy4 function call
        enemyd(enemyx4,enemyy4)
    elif enemyy4>=631:
        x+=1
        if x>0:
            enemyy_change4=-160
        enemyy4=enemyy_change4
        #enemy4 function call
        enemyd(enemyx4,enemyy4)
    #Enemy5 Movement
    if enemyy5<=631:
        x=0
        if x==0:
            enemyy_change5=2
        enemyy5+=enemyy_change5
        #enemy5 function call
        enemye(enemyx5,enemyy5)
    elif enemyy5>=631:
        x+=1
        if x>0:
            enemyy_change5=-240
        enemyy5=enemyy_change5
        #enemy4 function call
        enemye(enemyx5,enemyy5)
    #player function call
    playerfn(playerx,playery)
    #game update
    pygame.display.update()
pygame.quit()
