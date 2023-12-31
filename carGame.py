import pygame
import time
import random

pygame.init()

#including sound
#crash_sound = pygame.mixer.Sound("music.mp3")
pygame.mixer.music.load("music.mp3")

#display size
display_width = 800
display_height = 600

#colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Let's Begin the Race")
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
gameIcon = pygame.image.load('game.png')

pygame.display.set_icon(gameIcon)

pause = False
#crash = True

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms",25)
    text = font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():

    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit", 550,450,100,50,red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect = text_objects(msg,smallText)
        textRect.center=((x+(w/2)),(y+(h/2)))
        gameDisplay.blit(textSurf,textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit", 550,450,100,50,red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText=pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("Let's Begin the Race",largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Go!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

    pygame.mixer.music.play(-1)

    x = (display_width*0.45)
    y = (display_height*0.8)

    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, None)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

game_intro()