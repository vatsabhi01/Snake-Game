import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
display_width = 600
display_height = 400
red = (255,0,0)
green = (0,255,0)
blue = (0,0,50)
black =(0,0,0)
orange = (255,123,7)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("snake game")


snake = 10
snakeSpeed= 15
snakelist=[]
def snakeFunc(snake,snakelist):
    for x in snakelist:
        pygame.draw.rect(gameDisplay, orange, [x[0], x[1], snake, snake])
def snakegame():
    game = False
    gameend=False
    x1 = display_width/2
    y1 = display_height/2
    x1change = 0
    y1change = 0

    snakelist=[]
    lengthOfSnake=1

    foodx = round(random.randrange(0, display_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake) / 10.0) * 10.0
    while not game:

        while gameend==True:
            gameDisplay.fill(blue)
            font_style = pygame.font.SysFont("comicsansms",25)
            message= font_style.render("You Lost :( !!! Wanna Play Again, Press S",True, red)
            gameDisplay.blit(message,[display_width/6,display_height/3])
            font_style = pygame.font.SysFont("comicsansms", 25)
            message = font_style.render("Press Q to Exit", True, red)
            gameDisplay.blit(message, [display_width / 6, display_height / 2])


            score = lengthOfSnake-1
            scorefont=pygame.font.SysFont("comicsansms",35)
            value= scorefont.render("Your Score = " + str(score), True, green)
            gameDisplay.blit(value, [display_width/3, display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        snakegame()
                    if event.key == pygame.K_q:
                        game = True
                        gameend = False

                if event.type == pygame.QUIT:
                    game=True
                    gameend=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game=True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    y1change= snake
                    x1change =0
                elif event.key == pygame.K_UP:
                    y1change = -snake
                    x1change = 0
                elif event.key == pygame.K_LEFT:
                    x1change = -snake
                    y1change=0
                elif event.key == pygame.K_RIGHT:
                    x1change = snake
                    y1change=0
        if x1>=display_width or x1 < 0 or y1 >=display_height or y1 < 0:
            gameend=True
        x1 += x1change
        y1 += y1change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, green, [foodx,foody, snake, snake])
        snakeHead=[]
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakelist.append(snakeHead)
        if len(snakelist)>lengthOfSnake:
            del snakelist[0]

        for x in snakelist[:-1]:
            if x==snakeHead:
                gameend=True
        snakeFunc(snake,snakelist)

        if x1 == foodx and y1==foody:
            foodx = round(random.randrange(0, display_width-snake)/10.0)*10.0
            foody = round(random.randrange(0, display_height - snake)/10.0)*10.0
            lengthOfSnake +=1
        pygame.display.update()
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
snakegame()