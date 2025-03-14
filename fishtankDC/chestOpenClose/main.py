
import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("fish mouse imput")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
chest = 1
ticker = 0

fishyboi = 1
fishyticker = 0

fishyboiImg = pygame.image.load("C:\\Users\\797074\\Desktop\\Python_DailyCodes\\fishtankDC\\chestOpenClose\\fishyboi.png").convert_alpha()
pygame.Surface.set_colorkey(fishyboiImg, [255,0,255])
fishyboiImg2 = pygame.image.load("C:\\Users\\797074\\Desktop\\Python_DailyCodes\\fishtankDC\\chestOpenClose\\fishyboi2.png").convert_alpha()
pygame.Surface.set_colorkey(fishyboiImg2, [255,0,255])

#load in the image and make transparent
chestImg1 = pygame.image.load("C:\\Users\\797074\\Desktop\\Python_DailyCodes\\fishtankDC\\chestOpenClose\\chest1.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg1, [255,0,255])
#load in the image and make transparent
chestImg2 = pygame.image.load("C:\\Users\\797074\\Desktop\\Python_DailyCodes\\fishtankDC\\chestOpenClose\\chest2.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg2, [255,0,255])

running = True
while running: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #print(mousePos) #this is to help you know where to set these boundaries
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #check if you've clicked on the chest
            if mousePos[0]>238 and mousePos[0] < 355 and mousePos[1]>130 and mousePos[1]<230:
               chest = 2
            
            if mousePos[0]> 400 and mousePos[0] <600 and mousePos[1] > 300 and mousePos[1] < 460:
                fishyboi = 2
            
         
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos        
    
    #update/physics section----------------------

    #keep chest open for 50 game loops:
    if chest == 2:
        ticker+=1
        if ticker >= 200:
            ticker = 0
            chest = 1


    if fishyboi == 2:
        fishyticker+=1
        if fishyticker >= 200:
            fishyticker = 0
            fishyboi = 1

    #render section------------------------------
    
    screen.fill((0,0,180))# Clear the screen
    
    #draw background image
    if chest == 1:
        screen.blit(chestImg1, (240, 140))
    elif chest ==2: 
        screen.blit(chestImg2, (240, 140))

    if fishyboi == 1:
        screen.blit(fishyboiImg, (400, 300))
    elif fishyboi ==2: 
        screen.blit(fishyboiImg2, (400, 300))

    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()

