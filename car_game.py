import pygame
import time
import random
pygame.init()

green = (0, 190, 0)
bright_green = (0, 255, 0)
red = (190, 0, 0)
bright_red = (255, 0, 0)
blue = (0, 0, 190)
bright_blue = (0, 0, 255)
white = (190, 190, 190)
bright_white = (255, 255, 255)
pink = (255,192,203)
bright_pink = (231, 84, 128)
black = (60, 60, 60)
bright_black = (0, 0, 0)
violet = (238,130,238)
bright_violet = (48,25,52)
grey = (128, 128, 128)

display_width = 800
display_height = 600
car_height = 125
car_width = 56
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")
carimg = pygame.image.load('car1.jpg')
greenimg = pygame.image.load('green patch.jpg')
yellow_strip = pygame.image.load('yellow strip.jpg')
strip = pygame.image.load('strip.jpg')
intro_bg = pygame.image.load('intro_bg.jpg')
instruct_bg = pygame.image.load('instruct_bg.jpg')
clock = pygame.time.Clock()
pause = False
select = -1
highest = 0

#To display text
def text_display(text, font, color = (0, 0, 0)):
    text_var = font.render(text, True, color)
    text_rect = text_var.get_rect()
    return (text_var, text_rect)

#To display buttons
def button(disp,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "start":
                select_car()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "continue":
                game_loop()
            elif action == "instruct":
                instructed()
            elif action == "main":
                intro_loop()
            elif action == "unpaused":
                unpaused()
            elif action == "restart":
                game_loop()
            elif action == "in_game_instructed":
                in_game_instructed()
    else:
        pygame.draw.rect(gamedisplays, ic,(x,y,w,h))

    font = pygame.font.Font("freesansbold.ttf",20)
    text, text_rect = text_display(disp, font, (0, 0, 0))
    text_rect.center = ( (x+(w/2)), (y+(h/2)) )
    gamedisplays.blit(text, text_rect)

#To display a button with an image inside it
def buttonimg(butimg,x,y,w,h,ic,ac,action):
    global select
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
        if click[0] == 1:
            if action == 0:
                select = 0
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 1:
                select = 1
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 2:
                select = 2
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 3:
                select = 3
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 4:
                select = 4
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 5:
                select = 5
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
            elif action == 6:
                select = 6
                pygame.draw.rect(gamedisplays, ac,(x,y,w,h))

    else:
        if select == action:
            pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
        else:
            pygame.draw.rect(gamedisplays, ic,(x,y,w,h))

    gamedisplays.blit(butimg, (x+5, y+5))

#Defining the function for start page
def intro_loop():
    introvar = True
    while introvar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.quit()
        gamedisplays.blit(intro_bg, (0,0))
        font = pygame.font.Font("freesansbold.ttf", 50)
        text, text_rect = text_display("Car Game", font)
        text_rect.center = ((400, 100))
        gamedisplays.blit(text, text_rect)
        button("Start", 125, 500, 130, 60, green, bright_green, "start")
        button("Instructions", 335, 500, 130, 60, blue, bright_blue, "instruct")
        button("Quit", 545, 500, 130, 60, red, bright_red, "quit")
        pygame.display.update()
        clock.tick(50)

#Defining the instructions page
def instructed():
    instruct = True
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.quit()
        gamedisplays.blit(instruct_bg, (0, 0))
        instruction_text = pygame.font.Font("freesansbold.ttf", 70)
        text, text_rect = text_display("Instructions", instruction_text)
        text_rect.center = (400, 60)
        instruction_text1 = pygame.font.Font("freesansbold.ttf", 15)
        text1, text_rect1 = text_display("In this game, you need to avoid other vehicles on the road in order to gain points.", instruction_text1)
        text_rect1.center = (400, 130)
        instruction_text2 = pygame.font.Font("freesansbold.ttf", 50)
        text2, text_rect2 = text_display("Controls", instruction_text2)
        text_rect2.center = (400, 200)
        instruction_text3 = pygame.font.Font("freesansbold.ttf", 20)
        text3, text_rect3 = text_display("Left Arrow: Move Left", instruction_text3)
        text_rect3.left = 200
        #instruction_text4 = pygame.font.Font("freesansbold.ttf", 25)
        text4, text_rect4 = text_display("Right Arrow: Move Right", instruction_text3)
        text_rect4.left = 200
        #instruction_text5 = pygame.font.Font("freesansbold.ttf", 25)
        text5, text_rect5 = text_display("Up Arrow: Move Up", instruction_text3)
        text_rect5.left = 200
        #instruction_text6 = pygame.font.Font("freesansbold.ttf", 25)
        text6, text_rect6 = text_display("Down Arrow: Move Down", instruction_text3)
        text_rect6.left = 200
        #instruction_text7 = pygame.font.Font("freesansbold.ttf", 25)
        text7, text_rect7 = text_display("A: Accelarate", instruction_text3)
        text_rect7.left = 200
        text8, text_rect8 = text_display("B: Brake", instruction_text3)
        text_rect8.left = 200
        text9, text_rect9 = text_display("Space Bar: Pause", instruction_text3)
        text_rect9.left = 200
        gamedisplays.blit(text, text_rect)
        gamedisplays.blit(text1, text_rect1)
        gamedisplays.blit(text2, text_rect2)
        gamedisplays.blit(text3, (100, 250))
        gamedisplays.blit(text4, (100, 290))
        gamedisplays.blit(text5, (100, 330))
        gamedisplays.blit(text6, (100, 370))
        gamedisplays.blit(text7, (100, 410))
        gamedisplays.blit(text8, (100, 450))
        gamedisplays.blit(text9, (100, 490))
        button("Back", 600, 500, 130, 60, blue, bright_blue, "main")
        pygame.display.update()
        clock.tick(30)

#To display the page consisting of car choices from which the user can select his car to play the game
def select_car():
    sel = True
    while sel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruct_bg, (0,0))
        font = pygame.font.Font("freesansbold.ttf", 80)
        text, text_rect = text_display("Select Your Car", font)
        text_rect.center = (400, 150)
        gamedisplays.blit(text, text_rect)
        buttonimg(pygame.image.load('car.jpg'), 45, 300-5, car_width + 10, car_height + 10, white, bright_white, 0)
        buttonimg(pygame.image.load('car1.jpg'), 151, 300-5, car_width + 10, car_height + 10, white, bright_white, 1)
        buttonimg(pygame.image.load('car2.jpg'), 257, 300-5, car_width + 10, car_height + 10, white, bright_white, 2)
        buttonimg(pygame.image.load('car3.jpg'), 363, 300-5, car_width + 10, car_height + 10, white, bright_white, 3)
        buttonimg(pygame.image.load('car4.jpg'), 469, 300-5, car_width + 10, car_height + 10, white, bright_white, 4)
        buttonimg(pygame.image.load('car5.jpg'), 575, 300-5, car_width + 10, car_height + 10, white, bright_white, 5)
        buttonimg(pygame.image.load('car6.jpg'), 681, 300-5, car_width + 10, car_height + 10, white, bright_white, 6)
        button("Continue", 650, 500, 130, 60, bright_blue, blue, "continue")
        button("Back", 20, 500, 130, 60, blue, bright_blue, "main")
        pygame.display.update()
        clock.tick(30)
        select = False

#To set the background of the gaming window
def background():
    gamedisplays.blit(greenimg, (0,0))
    gamedisplays.blit(greenimg, (697,0))
    gamedisplays.blit(strip, (115, 0))
    gamedisplays.blit(strip, (677, 0))
    for i in range(7):
        gamedisplays.blit(yellow_strip, (375,i*100))

#To load the car based on user choice
def car(x, y):
    global select
    if select == 0:
        gamedisplays.blit(pygame.image.load('car.jpg'), (x, y))
    elif select == 1:
        gamedisplays.blit(pygame.image.load('car1.jpg'), (x, y))
    elif select == 2:
        gamedisplays.blit(pygame.image.load('car2.jpg'), (x, y))
    elif select == 3:
        gamedisplays.blit(pygame.image.load('car3.jpg'), (x, y))
    elif select == 4:
        gamedisplays.blit(pygame.image.load('car4.jpg'), (x, y))
    elif select == 5:
        gamedisplays.blit(pygame.image.load('car5.jpg'), (x, y))
    elif select == 6:
        gamedisplays.blit(pygame.image.load('car6.jpg'), (x, y))

#To display the score card on the gaming screen
def score_card(passed, score):
    global highest
    font = pygame.font.Font("freesansbold.ttf", 15)
    text = font.render("Passed: " + str(passed), True, (255, 0, 0))
    points = font.render("Score: " + str(score), True, (255, 0, 0))
    high_score = font.render("Best Score: " + str(highest), True, (255, 0, 0))
    gamedisplays.blit(text, (10, 10))
    gamedisplays.blit(points, (10, 30))
    gamedisplays.blit(high_score, (10, 50))

#To display other vehicles present on the road as when the function is called from the game_loop() function
def enemy(enemy_x, enemy_y, enemy_num):
    if enemy_num == 0:
        enemy_img = pygame.image.load('car.jpg')
    elif enemy_num == 1:
        enemy_img = pygame.image.load('car1.jpg')
    elif enemy_num == 2:
        enemy_img = pygame.image.load('car2.jpg')
    elif enemy_num == 3:
        enemy_img = pygame.image.load('car3.jpg')
    elif enemy_num == 4:
        enemy_img = pygame.image.load('car4.jpg')
    elif enemy_num == 5:
        enemy_img = pygame.image.load('car5.jpg')
    elif enemy_num == 6:
        enemy_img = pygame.image.load('car6.jpg')
    gamedisplays.blit(enemy_img, (enemy_x, enemy_y))

#To display the countdown before the start of the game
def countdown():
    count = True
    while count:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.quit()
        gamedisplays.fill(grey)
        background()
        clock.tick(3)
        countdown_text = pygame.font.Font("freesansbold.ttf", 70)
        text, text_rect = text_display("3", countdown_text, bright_red)
        text_rect.center = (400, 300)
        gamedisplays.blit(text, text_rect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        background()
        text1, text_rect1 = text_display("2", countdown_text, bright_red)
        text_rect1.center = (400, 300)
        gamedisplays.blit(text1, text_rect1)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        background()
        text2, text_rect2 = text_display("1", countdown_text, bright_red)
        text_rect2.center = (400, 300)
        gamedisplays.blit(text2, text_rect2)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        background()
        text3, text_rect3 = text_display("Go!!!", countdown_text, bright_red)
        text_rect3.center = (400, 300)
        gamedisplays.blit(text3, text_rect3)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        background()
        count = False

#To continue the game after the user has paused it
def unpaused():
    global pause
    pause = False

#To display the page which will get loaded when the game is paused
def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(instruct_bg, (0, 0))
        instruction_text = pygame.font.Font("freesansbold.ttf", 70)
        text, text_rect = text_display("Paused", instruction_text)
        text_rect.center = (400, 300)
        button("Continue",125, 450, 130, 60,green, bright_green, "unpaused")
        button("Restart", 335, 450, 130, 60, blue, bright_blue, "restart")
        button("Start Page", 545, 450, 130, 60, red, bright_red, "main")
        gamedisplays.blit(text, text_rect)
        pygame.display.update()
        clock.tick(30)

#To display the page when the instructions button present on the gaming screen is clicked
def in_game_instructed():
    global pause
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.quit()
        gamedisplays.blit(instruct_bg, (0, 0))
        instruction_text = pygame.font.Font("freesansbold.ttf", 70)
        text, text_rect = text_display("Instructions", instruction_text)
        text_rect.center = (400, 60)
        instruction_text1 = pygame.font.Font("freesansbold.ttf", 15)
        text1, text_rect1 = text_display("In this game, you need to avoid other vehicles on the road in order to gain points.", instruction_text1)
        text_rect1.center = (400, 130)
        instruction_text2 = pygame.font.Font("freesansbold.ttf", 50)
        text2, text_rect2 = text_display("Controls", instruction_text2)
        text_rect2.center = (400, 200)
        instruction_text3 = pygame.font.Font("freesansbold.ttf", 20)
        text3, text_rect3 = text_display("Left Arrow: Move Left", instruction_text3)
        text_rect3.left = 200
        #instruction_text4 = pygame.font.Font("freesansbold.ttf", 25)
        text4, text_rect4 = text_display("Right Arrow: Move Right", instruction_text3)
        text_rect4.left = 200
        #instruction_text5 = pygame.font.Font("freesansbold.ttf", 25)
        text5, text_rect5 = text_display("Up Arrow: Move Up", instruction_text3)
        text_rect5.left = 200
        #instruction_text6 = pygame.font.Font("freesansbold.ttf", 25)
        text6, text_rect6 = text_display("Down Arrow: Move Down", instruction_text3)
        text_rect6.left = 200
        #instruction_text7 = pygame.font.Font("freesansbold.ttf", 25)
        text7, text_rect7 = text_display("A: Accelarate", instruction_text3)
        text_rect7.left = 200
        text8, text_rect8 = text_display("B: Brake", instruction_text3)
        text_rect8.left = 200
        text9, text_rect9 = text_display("Space Bar: Pause", instruction_text3)
        text_rect9.left = 200
        gamedisplays.blit(text, text_rect)
        gamedisplays.blit(text1, text_rect1)
        gamedisplays.blit(text2, text_rect2)
        gamedisplays.blit(text3, (100, 250))
        gamedisplays.blit(text4, (100, 290))
        gamedisplays.blit(text5, (100, 330))
        gamedisplays.blit(text6, (100, 370))
        gamedisplays.blit(text7, (100, 410))
        gamedisplays.blit(text8, (100, 450))
        gamedisplays.blit(text9, (100, 490))
        button("Continue", 600, 500, 130, 60, blue, bright_blue, "unpaused")
        pygame.display.update()
        clock.tick(30)

#To conclude the game when user's car hits another vehicle on the road
def crash(prev_highest):
    if highest > prev_highest and prev_highest != 0:
        font = pygame.font.Font("freesansbold.ttf", 25)
        text, text_rect = text_display("Congratulations!!! You have achieved a new high score.", font, bright_red)
        text_rect.center = (display_width/2, display_height/2)
        gamedisplays.blit(text, text_rect)
        pygame.display.update()
        time.sleep(3)
        gamedisplays.fill(grey)
        background()
        pygame.display.update()
    font1 = pygame.font.Font("freesansbold.ttf", 40)
    #font2 = pygame.font.Font("freesansbold.ttf", 25)
    text1 = font1.render("Game Over!!!", True, (255, 0, 0))
    #text2 = font2.render("Press any key to restart.", True, (0, 0, 255))
    text_rect1 = text1.get_rect()
    #text_rect2 = text2.get_rect()
    text_rect1.center = (display_width/2, display_height/2)
    #text_rect2.center = (display_width/2, (display_height+50)/2)
    gamedisplays.blit(text1, text_rect1)
    #gamedisplays.blit(text2, text_rect2)
    pygame.display.update()
    time.sleep(4)
    game_loop()

#Main screen where the game is actually played
def game_loop():
    global highest
    prev_highest = highest
    x = 372
    y = display_height*0.8
    x_change = 0
    y_change = 0
    enemy_height = 125
    enemy_width = 56
    enemy_x = random.randrange(120, 621)
    enemy_y = -enemy_height
    enemy_speed = 9
    enemy_num = random.randrange(0,7)
    bumped = False
    passed = 0
    score = 0
    level = 1
    flag = 0
    move = 0
    global pause
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = +5
                if event.key == pygame.K_UP:
                    y_change = -enemy_speed/3
                if event.key == pygame.K_DOWN:
                    y_change = enemy_speed/3
                if event.key == pygame.K_a:
                    enemy_speed += 1
                if event.key == pygame.K_b:
                    enemy_speed -= 1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        y = min(y, 475)
        y = max(y, 0)
        gamedisplays.fill((128, 128, 128))
        #background()

        if flag == 0:
            """fontl = pygame.font.Font("freesansbold.ttf", 40)
            textl = fontl.render("Level " + str(level), True, (255, 0, 0))
            text_rectl = textl.get_rect()
            text_rectl.center = (display_width/2, display_height/2)
            gamedisplays.blit(textl, text_rectl)
            pygame.display.update()
            time.sleep(2)"""
            countdown()
            flag = 1

        relative_y = move % greenimg.get_rect().width
        gamedisplays.blit(greenimg, (0, relative_y - greenimg.get_rect().width))
        gamedisplays.blit(greenimg, (697, relative_y - greenimg.get_rect().width))
        if relative_y < 800:
            gamedisplays.blit(greenimg, (0, relative_y))
            gamedisplays.blit(greenimg, (697, relative_y))
            for i in range(7):
                gamedisplays.blit(yellow_strip, (375, relative_y + i*100))
            ran = [-2, 0, 2]
            for i in ran:
                gamedisplays.blit(strip, (115, 0 + relative_y + 200*i))
                gamedisplays.blit(strip, (677, 0 + relative_y + 200*i))
        move += enemy_speed

        highest = max(score, highest)
        button("Instructions", 670, 0, 130, 60, blue, bright_blue, "in_game_instructed")
        score_card(passed, score)
        enemy_y -= enemy_speed/4
        enemy(enemy_x, enemy_y, enemy_num)
        enemy_y += enemy_speed
        car(x, y)

        if enemy_y > display_height:
            enemy_y = 0 - enemy_height
            enemy_x = random.randrange(120, 621)
            enemy_num = random.randrange(0,7)
            passed += 1
            score = passed*10
            if int(passed) % 10 == 0:
                enemy_speed+=2
                level += 1
                fontl = pygame.font.Font("freesansbold.ttf", 70)
                textl = fontl.render("Level " + str(level), True, (255, 0, 0))
                text_rectl = textl.get_rect()
                text_rectl.center = (display_width/2, display_height/2)
                gamedisplays.blit(textl, text_rectl)
                pygame.display.update()
                time.sleep(3)

        if x < 120 or x > 621:
            crash(prev_highest)

        if (y < enemy_y + enemy_height and enemy_y < y) or (y + enemy_height > enemy_y and y + enemy_height < enemy_y + enemy_height):
            if (x < enemy_x + enemy_width and x > enemy_x) or (x + enemy_width > enemy_x and x + enemy_width < enemy_x + enemy_width):
                crash(prev_highest)

        pygame.display.update()
        clock.tick(60)

intro_loop()
pygame.quit()
quit()
