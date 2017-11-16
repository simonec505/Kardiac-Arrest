#-------------------------------------------------------------------------------
# Name:        Kardiac_Arrest ('K' initial intentional)
# Purpose:     SI 224 - project
#
# Author:      Simone Coetzer 16538471
#
# Created:     Apr/May 2015
#-------------------------------------------------------------------------------

#setup modules for use
import pygame
import time
import random
pygame.init()

#set colours for use in fonts
grey = (55, 55, 55)
white = (255,255,255)

#set unchanging properties of main character, heart (what the character strives
# for), and cloud (obstacle).
char_width = 100
char_height = 116
heart_width = 117
heart_height = 108
cloud_width = 530
cloud_height = 5 #this is not the cloud image's real height. This height does however suffice to make it look realistic when she 'crashes' into the cloud

#set window properties
display_width = 1200
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kardiac_Arrest')
clock = pygame.time.Clock()

#load images for use in game
menu_background = pygame.image.load('menu_background.jpg')
menu_button1 = pygame.image.load('menu_button1.png')
menu_button2 = pygame.image.load('menu_button2.png')
menu_button1_hover = pygame.image.load('menu_button1_hover.png')
charImg1 = pygame.image.load('character1.png')
charImg = pygame.image.load('character2.png')
heartImage1 = pygame.image.load('heart1.png')
cloudImg1 = pygame.image.load('cloud1.png')
gameloop_background = pygame.image.load('gameloop_background.jpg')

# The following functions make use of Pygame's 'blit' function to 'paste' images
# and text to the screen. x and y coordinates are sometimes used as parameters.
# In the game_loop() function, these parameters will receive arguments to 'paste'
# the image to the correct part of the screen (if the image requires to be moved
# along the x and y axis).
def heart(heart_x, heart_y):
    gameDisplay.blit(heartImage1,(heart_x, heart_y))

def clouds(cloud_startx, cloud_y):
    gameDisplay.blit(cloudImg1,(cloud_startx, cloud_y))

def game_background():
    gameDisplay.blit(gameloop_background, (0,0))

def char(char_x, char_y):
    gameDisplay.blit(charImg, (char_x,char_y))

def char1(char_x,char_y):
    gameDisplay.blit(charImg1, (char_x, char_y))

def show_char(char_x, char_y):
    char(char_x,char_y)
    pygame.display.update()
    clock.tick(80)
    gameDisplay.fill(white)

def displayScore(score):
    font = pygame.font.SysFont("Forte", 45)
    text = font.render("Hearts Won: " + str(score), True, white)
    gameDisplay.blit(text, (20, 20))

#this function is called in the scoreboard() function.
def high_score_message(currentScore, all_scores):
#if user's score is bigger than first 3 biggest scores, then user has a high score
        if int(currentScore) > all_scores[2]:
            text1 = "HIGH SCORE!"

        elif int(currentScore) == all_scores[2]:
            text1 = "Highscore Tie!"
        else:
            text1 = "No Highscore"

        return text1

# The play_button() function is called repeatedly at certain points in the game
# to let the game_loop() function start again. The numbers delimit the edges
# of the button.
def play_button():
    pointer_pos = pygame.mouse.get_pos()
    select = pygame.mouse.get_pressed()

    if 645 > pointer_pos[0] > 500 and 300 < pointer_pos[1] < 400:
        #if the person hovers over the button:
        gameDisplay.blit(menu_background, (0,0))
        gameDisplay.blit(menu_button1_hover, (500,300))
        if select[0] == 1:
            #if the person clicks on the button:
            gameDisplay.blit(menu_background, (0,0))
            gameDisplay.blit(menu_button2, (500,300))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    #as soon as the person's finger releases the button:
                    game_loop()

#The following function stipulates what should happen in the start menu
def start_menu():

    #background music
    pygame.mixer.music.load("In_Love.ogg")
    pygame.mixer.music.play(-1, 0.0)

    #infinite loop can only stop when user presses 'quit' button or when user
    #presses play button to go into game_loop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menu_background, (0,0))
        gameDisplay.blit(menu_button1, (500, 300))

        play_button()

        font = pygame.font.SysFont("Forte", 70)
        text1 = font.render("Kardiac_Arrest", True, grey)
        gameDisplay.blit(text1, (370, 120))

        font = pygame.font.SysFont("Forte", 45)
        text2 = font.render("Play", True, grey)
        gameDisplay.blit(text2, (530, 400))

        pygame.display.update()
        clock.tick(30)


def game_loop():

    # These variables will change in the while loop
    score = 0

    cloud_y = 330
    cloud_startx = 1300

    heart_y = 130
    heart_x = 1300

    loop_counter = 0 #used in a later if statement which makes it look as if the girl is running

    while True:

        #these variables ensure that the hearts and the clouds do not move at a
        #constant speed (this is to make the game more difficult)
        heart_speed = random.randrange(-30,-14, 5)
        cloud_speed = random.randrange(-20, -10, 5)

        #These variables will change in the for loop (when the girl jumps)
        char_x = (display_width * 0.15)
        char_y = (display_height * 0.55)
        y_change = 0 #the amount by which the y-coordinate changes

        # this var used in a later if statement which makes it look as if the girl is running
        loop_counter += 1

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # input validation
            if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
                        input(str("You need to hold down space bar to jump. Press any key and 'enter' to continue: "))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                #If user presses down the spacebar:
                    for i in range (46,0,-1): #when the character jumps up

                        #to create the illusion of gravity, the y-change must
                        #change every time
                        y_change = -i*0.2
                        char_y += y_change

                        #show game objects on the screen
                        show_char(char_x, char_y)
                        game_background()

                        clouds(cloud_startx, cloud_y)
                        cloud_startx += cloud_speed

                        heart(heart_x, heart_y)
                        heart_x += heart_speed

                        displayScore(score)

                        #call cloud and heart again if not visible anymore
                        if cloud_startx < -550:
                            cloud_startx = random.randrange(1200, 4000) #to add
                            #unexpectedness

                        if heart_x < -50:
                            heart_x = 1200

                        # if character 'wins' a heart, add to score
                        if (char_x + char_width >= heart_x and char_x <= heart_x + heart_width) and (char_y <= heart_y + heart_height and char_y + char_height >= heart_y ):
                            score = score + 1
                            heart_y = random.randrange(100, 150) #makes heart 'wiggle' when caught.
                            cloud_speed = cloud_speed - 0.2

                        # if character gets 'stuck in the clouds', write score to
                        # necessary files and go to scoreboard()
                        if ((char_x >= cloud_startx and char_x <= cloud_startx + cloud_width) and (char_y >= cloud_y and y <= cloud_y + cloud_height)) or ((char_x + char_width >= cloud_startx and char_x + char_width <= cloud_startx + cloud_width) and (char_y + char_height >= cloud_y and char_y + char_height <= cloud_y +cloud_height)) :

                            currentScores_file = open('current_score.txt','w')
                            currentScores_file.write(str(score))
                            currentScores_file.close()

                            allScores_file = open('all_scores.txt','a')
                            allScores_file.write(str(score) + '\n')
                            allScores_file.close()

                            scoreboard()


                    for i in range (0,47): #when the character comes down


                        y_change = i*0.2 #gravity
                        char_y += y_change

                        # show objects of game
                        show_char(char_x, char_y)

                        game_background()

                        clouds(cloud_startx, cloud_y)
                        cloud_startx += cloud_speed

                        heart(heart_x, heart_y)
                        heart_x += heart_speed

                        displayScore(score)

                        #call cloud and heart again if out of view

                        if cloud_startx < -550:
                            cloud_startx = random.randrange(1200, 2200)

                        if heart_x < -50:
                            heart_x = 1200

                        #if character wins heart. add to score
                        if (char_x + char_width >= heart_x and char_x <= heart_x + heart_width) and (char_y <= heart_y + heart_height and char_y + char_height >= heart_y ):
                            score = score + 1
                            heart_y = random.randrange(100, 150)
                            cloud_speed = cloud_speed - 0.2 #to make the game
                            #more difficult, the clouds' speed increases

                        # if character gets 'stuck' in the clouds, write score to
                        # files and go to scoreboard()
                        if ((char_x >= cloud_startx and char_x <= cloud_startx + cloud_width) and (char_y >= cloud_y and char_y <= cloud_y + cloud_height)) or ((char_x + char_width >= cloud_startx and char_x + char_width <= cloud_startx + cloud_width) and (char_y + char_height >= cloud_y and char_y + char_height <= cloud_y +cloud_height)) :
                            currentScores_file = open('current_score.txt','w')
                            currentScores_file.write(str(score))
                            currentScores_file.close()

                            allScores_file = open('all_scores.txt','a')
                            allScores_file.write(str(score) + '\n')
                            allScores_file.close()

                            scoreboard()

                        ##evaluate_if_crashed(x, cloud_startx, cloud_y, cloud_width, cloud_height, y)


        #this if-statements makes it appear as if she's running.
        if loop_counter % 10 == 0 or loop_counter % 10 == 1 or loop_counter % 10 == 2 or loop_counter % 10 == 3 or loop_counter == 4: #condition used to make her move slowly
            #show game objects
            game_background()

            clouds(cloud_startx, cloud_y)
            cloud_startx += cloud_speed

            heart(heart_x, heart_y)
            heart_x += heart_speed

            displayScore(score)
            char(char_x, char_y)

        else:
            #show game objects
            game_background()

            clouds(cloud_startx, cloud_y)
            cloud_startx += cloud_speed

            heart(heart_x, heart_y)
            heart_x += heart_speed

            displayScore(score)
            char1(char_x, char_y)



        #call cloud and heart when they're not visible anymore

        if cloud_startx < -550:
            cloud_startx = random.randrange(1200, 2200)

        if heart_x < -50:
            heart_x = random.randrange(1200, 2200)

        #if girl gets stuck in cloud, write score to necessary files and go to
        # scoreboard()

        if ((char_x >= cloud_startx and char_x <= cloud_startx + cloud_width) and (char_y >= cloud_y and char_y <= cloud_y + cloud_height)) or ((char_x + char_width >= cloud_startx and char_x + char_width <= cloud_startx + cloud_width) and (char_y + char_height >= cloud_y and char_y + char_height <= cloud_y +cloud_height)) :

            currentScores_file = open('current_score.txt','w')
            currentScores_file.write(str(score) + '\n')
            currentScores_file.close()

            allScores_file = open('all_scores.txt','a')
            allScores_file.write(str(score) + '\n')
            allScores_file.close()

            scoreboard()

        pygame.display.update()
        clock.tick(60)

#This function shows the user their score and it calculates whether or not the person
# has a High Score (score is in top 3). It also gives the user the option to try again
def scoreboard():
    #let user know that the game is over
    gameDisplay.blit(menu_background, (0,0))

    font = pygame.font.SysFont("Forte", 70)
    text = font.render("GAME OVER", True, grey)
    gameDisplay.blit(text, (375, 260))

    pygame.display.update()
    time.sleep (2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menu_background, (0,0))
        gameDisplay.blit(menu_button1, (500, 300))

        play_button() #retry button

        font = pygame.font.SysFont("Forte", 45)
        text = font.render("Try Again", True, grey)
        gameDisplay.blit(text, (485, 400))

        currentScore_file = open('current_score.txt', 'r')
        currentScore = currentScore_file.readline()
        currentScore_file.close()

        # read all values from the all_scores.txt file
        allScores_file = open('all_scores.txt', 'r')
        all_scores = []
        index = 0
        # append read values to the all_scores array
        for line in allScores_file:
            all_scores.append(int(line))
        #sort values in descending order (so as to find largest 3 values)
        all_scores = sorted(all_scores, reverse = True)

        #display whether or not user got a highscore
        font = pygame.font.SysFont('Forte', 75)
        result_text = font.render(high_score_message(currentScore, all_scores), True, grey)
        gameDisplay.blit(result_text, (375, 180))

        allScores_file.close()

        font = pygame.font.SysFont('Forte', 40)
        text = font.render("Hearts Won: " + currentScore, True, grey)
        gameDisplay.blit(text, (460, 80))

        pygame.display.update()
        clock.tick(30)

start_menu()









