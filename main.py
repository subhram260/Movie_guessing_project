import sys
import time

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))



def text(x,y,text,size,font,color=(0,0,0)):
    font=pygame.font.Font(font,size)
    display=font.render(text,True,color)
    screen.blit(display,(x,y))
def score(point):
    text(380,110,'POINTS : '+str(point),23,None)
def drawtext(x,y,text,size,font):
    font = pygame.font.Font(font, size)
    score = font.render(text, True, "#352727")
    w=score.get_rect(center =(500/2,y))
    screen.blit(score,w)#(x,y))
def pl(n,movie,choice,length_movie,point,warn):
    not1 = 0
    for i in range(0, length_movie):
        if n == movie[i]:
            not1 = 1
            choice[i] = n
        else:
            {}
        if not1 == 0:
            point = point - 1
            #score(point)
            warn="letter is not present in the name"
        else:
            warn=""


def finalloop(movie,choice):
    resulting=True
    mov=""
    while resulting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resulting = False
                sys.exit()
            screen.fill('#ffffff')
            if movie==choice:
                #text(20,200,"g".upper()+"movie name is :"+mov.join(movie),30,None)
                drawtext(20, 200, "guess successfully ".upper(), 14, "result")
                drawtext(20, 240, "The movie name is  :  ".upper(), 17, "result")
                drawtext(20, 270, mov.join(movie).upper(), 17, "result")
            else:
                drawtext(20,200,"you loss the game ".upper(),14,"result")
                drawtext(20,240,"The correct movie name is  :  ".upper(),17,"result")
                drawtext(20,270,mov.join(movie).upper(),17,"result")
            pygame.draw.rect(screen, "#4b2660", (20, 32, 460, 433), 3)
        pygame.display.update()


def Playloop():
    playing=True
    movielist=["The Red Balloon","The Phone Call","Session Man","Hotel Chevalier","Small Deaths","Glory At Sea","Eight","Lick The Star","Carne","Crossroads"]
    movie=random.choice(movielist)
    movie=list(movie.upper())
    movie_length=len(movie)
    choice = []
    point=10
    mov=""
    typo = False
    end = False
    user_text=""
    length_text=0

    warn=""
    for i in movie:
        choice.append(" __ ")
        print("__", end=" ")
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing=False
                sys.exit()
            screen.fill('#ffffff')
            pygame.draw.rect(screen, '#57c2f7', (20, 32, 460, 433), 3)
            text(150,50,"GUESS THE MOVIE NAME",20,'abc','#09641d')
            pygame.draw.line(screen,'#57c2f7',(20,90),(480,90),3)
            pygame.draw.rect(screen, (0, 0, 0), (175, 400, 150, 50))
            text(218, 415, "check", 20, 'aAkarRumput.ttf.ttf', (233, 123, 0))
            pygame.draw.rect(screen, (0, 0, 0), (200, 280, 100, 30), 3)
            pos=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pos[0] > 175 and pos[0] < 325 and pos[1] > 400 and pos[1] < 450):
                    pygame.draw.rect(screen, (233, 123, 0), (175, 400, 150, 50), 5)
                    text(218, 415, "check", 20, 'aAkarRumput.ttf.ttf', (233, 123, 0))
                    #point=point-1
                    n = user_text
                    n = n.upper()
                    user_text=""
                    drawtext(20 - length_text, 250, user_text, 20, None)
                    #not1=pl(n, movie, choice, movie_length, point, warn)
                    not1 = 0
                    for i in range(0, movie_length):
                        if n == movie[i]:
                            not1 = 1
                            choice[i] = n
                        else:
                            {}
                    if not1 == 0:
                        point = point - 1
                        # score(point)
                        warn = "letter is not present in the name"
                    else:
                        warn = ""
                    if (movie == choice or point == 0):
                        playing=False
                        finalloop(movie,choice)
                    # point, warn = pl(n, movie, choice, movie_length, point, warn)
                    # running=False
                    # Playloop()
           # if event.type == pygame.MOUSEBUTTONUP:
           #     if (pos[0] > 175 and pos[0] < 325 and pos[1] > 400 and pos[1] < 450):
            #        j=0
            if event.type == pygame.MOUSEBUTTONUP:
                    if (pos[0] > 200 and pos[0] < 300 and pos[1] > 280 and pos[1] < 310):
                         typo=True
                    else:
                        typo=False
            if event.type == pygame.KEYDOWN:
                if end==False:
                    if event.key == pygame.K_BACKSPACE:
                         user_text =" "+user_text[:-1]+" "
                    elif event.key == pygame.K_RETURN:

                        n = user_text
                        n = n.upper()
                        user_text = ""
                        drawtext(20 - length_text, 250, user_text, 20, None)
                        #pl(n,movie,choice,movie_length,point,warn)
                        not1 = 0
                        for i in range(0, movie_length):
                            if n == movie[i]:
                                not1 = 1
                                choice[i] = n
                            else:
                                {}

                        if not1 == 0:
                            point = point - 1
                            # score(point)
                            warn = "letter is not present in the name".upper()
                        else:
                            warn = ""
                        if (movie == choice or point == 0):
                            playing=False
                            finalloop(movie,choice)
                    #    point,warn=pl(n,movie,choice,movie_length,point,warn)
                    elif typo:
                        user_text += event.unicode



            score(point)
            length_text = (movie_length // 2)*10
            drawtext(20-length_text , 200, mov.join(choice), 25, None)
            drawtext(20-length_text , 253, "Enter one letter to be filled in its correct place :".upper(), 20, None)
            drawtext(20-length_text , 294, user_text, 20, None)
            drawtext(20 - length_text, 334, warn, 25, None)


            
        pygame.display.update()


def mainloop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                sys.exit()
            screen.fill('#ffffff')
            pygame.draw.rect(screen,(233,123,0),(20,32,460,433),3)
            text(50,60,"GUESSING MOVIE NAME",39,'aAkarRumput.ttf.ttf')
            text(55,200,"Firstly you have 10 points, if you guess one wrong  ",13,'BabaPro-Bold')
            text(71,220,"letter then one point is detected each time , If  ",13,'BabaPro-Bold')
            text(107,240,"you guess right name then you win   ",13,'BabaPro-Bold')
            text(163,260,"otherwise you lose.  ",13,'BabaPro-Bold')
            pygame.draw.rect(screen,(0,0,0),(175,400,150,50))
            text(208,415,"START -->",20,'aAkarRumput.ttf.ttf',"#ffffff")
            pose=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if (pose[0] > 175 and pose[0] < 325 and pose[1] > 400 and pose[1] < 450):
                    #pygame.draw.rect(screen, (233, 123, 0), (175, 400, 150, 50), 3)
                    text(208, 415, "START -->", 20, 'aAkarRumput.ttf.ttf', (233, 123, 0))
                else:
                    # text(208, 415, "START -->", 20, 'aAkarRumput.ttf.ttf', "#ffffff")
                    {}
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if (pose[0]>175 and pose[0]<325 and pose[1]>400 and pose[1]<450):
                    pygame.draw.rect(screen, (233,123,0), (175, 400, 150, 50),5)
                    text(208, 415, "START -->", 20, 'aAkarRumput.ttf.ttf', (233,123,0))
                    #running=False
                    #Playloop()
                    running = False
                    Playloop()
            if event.type ==pygame.MOUSEBUTTONUP:
                if (pose[0]>175 and pose[0]<325 and pose[1]>400 and pose[1]<450):
                    #pygame.draw.rect(screen, (233,123,0), (175, 400, 150, 50),5)
                    #text(208, 415, "START -->", 20, 'aAkarRumput.ttf.ttf', (233,123,0))
                    {}
        pygame.display.update()


mainloop()