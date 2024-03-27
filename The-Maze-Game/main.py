# Aabjosh Singh
# The Maze Game - Open End Project
# Pygame output file

# Imports pygame, time for debounce, and custom files for use
import pygame, sys
import time
import maze_solver
import prim_maze_generation

from pygame.locals import QUIT

# Initializing variables, lists, colours, and display size
br = (68, 173, 246)
colour1 = (80,80,100)
GreenPath = (93,255,50)
colour2 = (5,225,75)
buttonmain = (255, 75, 100)
buttonhover = (255, 160, 185)
colour5 = (217,215,221)
windowback = (151, 155, 171)
windowborder = (193, 184, 200)
currentposition = (195, 50, 75)
usercolour = (242,221,110)
currentbuttoncolourreturn = buttonmain
titlecolour = buttonmain
y_textfieldcolour = buttonmain
x_textfieldcolour = buttonmain
y_currentcolour = br
y_buttontext = 'OK'
x_currentcolour = br
x_buttontext = 'OK'
# (242, 221, 110)

DISPLAYSURF = pygame.display.set_mode((1000, 500))

width = DISPLAYSURF.get_width()
height = DISPLAYSURF.get_height()
menucondition = True
sliderpos = 55
lightmode = True
mazeinit = False
solved = False
solved_by_user = False
popupcustomcondition = False
y_textfieldcase = False
x_textfieldcase = False
keypress = False
errorcondition = False
x_passedcustom = False
y_passedcustom = False
hotcoldexecute = False
instructioncase = False
displaymode = "Light Mode"
mazeborder_x = 250
mazeborder_y = 125
mazemode = ''
y_usertext = ''
x_usertext = ''

LocalMaze = []
positions = []
userpositions = []
start = []
end = []
playerpos = []
easy_scores_list = []
moderate_scores_list = []
hard_scores_list = []
custom_scores_list = []

# Initializing images and icons, as well as the caption, fonts, a game title...
mazeicon = pygame.image.load('rubik.png')

mazebr = pygame.image.load('mazebrsquare.png')

userposicon = pygame.image.load('userposition.png')

instructions = pygame.image.load('How-To-Play.png')

pygame.init()
pygame.display.set_caption(' The Maze Game')
pygame.display.set_icon(mazeicon)



fontheading = pygame.font.SysFont('Poppins-SemiBold.ttf', 45)
fontnormal = pygame.font.SysFont('Poppins-Light.ttf', 25)
title = fontheading.render('The Maze Game', True, titlecolour)
textposition = title.get_rect()
textposition.center = (500, 110)
pygame.display.flip()

# Displays the main menu to start
DISPLAYSURF.fill(br)
DISPLAYSURF.blit(mazebr, (485,-5))
DISPLAYSURF.blit(mazebr, (5,-5))

sliderrect = pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(50, 425, 60, 30), 0, 25)

menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
        
menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
        
selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)

moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
displaymode = 'Light Mode'
modetext = fontnormal.render(displaymode, True, colour5)
modetextposition = modetext.get_rect()
modetextposition.center = (80, 470)
DISPLAYSURF.blit(modetext, modetextposition)

# Light/dark mode slider displayed/updated and title is shown if not in the popupcustomcondition (making custom maze menu)
def menudisplay():
    global fontheading
    global fontnormal
    global title
    global textposition
    global popupcustomcondition
    
    sliderrect = pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(50, 425, 60, 30), 0, 25)
    
    sliderpoint = pygame.draw.rect(DISPLAYSURF, colour5, pygame.Rect(sliderpos, 430, 20, 20), 0, 25)
    if not popupcustomcondition:
        title = fontheading.render('The Maze Game', True, titlecolour)
        textposition = title.get_rect()
        textposition.center = (500, 110)
        DISPLAYSURF.blit(title, textposition)

# Menu that shows the instructions on how to play the game (image) until escape is clicked
def instructionmenu():
    global DISPLAYSURF
    global instructioncase
    global br
    global mazebr
    global windowborder
    global windowback
    global colour5

    DISPLAYSURF.fill((255,255,255))
    DISPLAYSURF.blit(instructions, (162.5,30))
    entertext = fontnormal.render('Press \'Escape\'/\'Esc\' to exit...', True, (0,150,225))
    DISPLAYSURF.blit(entertext, (10,5))
    
    pygame.display.flip()
    
    press = pygame.key.get_pressed()

    if press[pygame.K_ESCAPE]:
        DISPLAYSURF.fill(br)
        DISPLAYSURF.blit(mazebr, (485,-5))
        DISPLAYSURF.blit(mazebr, (5,-5))
        menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
    
        menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
        
        selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
    
        
        moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
    
        modetext = fontnormal.render(displaymode, True, colour5)
        modetextposition = modetext.get_rect()
        modetextposition.center = (80, 470)
        DISPLAYSURF.blit(modetext, modetextposition)
        instructioncase = False

# The function that takes care of the user input for a custom maze in a separate menu, while giving the user the option to return to the main menu and also change colour themes
def popupcustom():
    global titlecolour
    global colour1
    global GreenPath
    global colour2
    global buttonmain
    global buttonhover
    global colour5
    global windowback
    global windowborder
    global DISPLAYSURF
    global width
    global height
    global menucondition
    global sliderpos
    global lightmode
    global clicks
    global LocalMaze
    global correctpositions
    global mazeinit
    global mazemode
    global usercolour
    global popupcustomcondition
    global y_textfieldcolour
    global x_textfieldcolour
    global y_usertext
    global x_usertext
    global y_textfieldcase
    global x_textfieldcase
    global keypress
    global errorcondition
    global y_currentcolour
    global y_buttontext
    global x_currentcolour
    global x_buttontext
    global y_passedcustom
    global x_passedcustom
    global positions 
    global userpositions 
    global start 
    global end 
    global playerpos 
    global solved 
    global solved_by_user 
    global currentbuttoncolourreturn
    global y_textfield
    global x_textfield

    if popupcustomcondition:
        # Title
        title = fontheading.render('Initialize Custom Maze', True, titlecolour)
        textposition = title.get_rect()
        textposition.center = (500, 110)
        DISPLAYSURF.blit(title, textposition)

        # Display coloured text boxes if not typing/not clicked on
        if not y_textfieldcase:
            y_textfield = pygame.draw.rect(DISPLAYSURF, y_textfieldcolour, pygame.Rect(350, 215, 250, 35), 0, 20)
            y_usertext_rendered = fontnormal.render(y_usertext, True, (0,0,0))
            DISPLAYSURF.blit(y_usertext_rendered,(355,225))
        if not x_textfieldcase:
            x_textfield = pygame.draw.rect(DISPLAYSURF, x_textfieldcolour, pygame.Rect(350, 335, 250, 35), 0, 20)
            x_usertext_rendered = fontnormal.render(x_usertext, True, (0,0,0))
            DISPLAYSURF.blit(x_usertext_rendered,(355,345))

        # Initialize the x and y custom size verification buttons
        custom_y_button = pygame.draw.rect(DISPLAYSURF, y_currentcolour, pygame.Rect(610, 215, 45, 35), 0, 20)
        custom_y_text = fontnormal.render(y_buttontext, True, colour5)
        custom_y_button_pos = custom_y_text.get_rect()
        custom_y_button_pos.center = custom_y_button.center
        DISPLAYSURF.blit(custom_y_text, custom_y_button_pos)
      
        custom_x_button = pygame.draw.rect(DISPLAYSURF, x_currentcolour, pygame.Rect(610, 335, 45, 35), 0, 20)
        custom_x_text = fontnormal.render(x_buttontext, True, colour5)
        custom_x_button_pos = custom_x_text.get_rect()
        custom_x_button_pos.center = custom_x_button.center
        DISPLAYSURF.blit(custom_x_text, custom_x_button_pos)

        # Initialize the button to return to the main menu
        buttonreturn = pygame.draw.rect(DISPLAYSURF, currentbuttoncolourreturn,       pygame.Rect(800, 230, 160, 40), 0, 10)
        returntext = fontnormal.render('Return To Menu', True, colour5)
        returnposition = returntext.get_rect()
        returnposition.center = buttonreturn.center
        DISPLAYSURF.blit(returntext, returnposition)
      
        pygame.display.flip()

        # Make the return button lighter if the cursor is on it
        if buttonreturn.collidepoint(cursor):
            currentbuttoncolourreturn = buttonhover

            # If the return button is clicked, reset vars and return to the main menu by displaying the starting content and ending popupcustomcondition
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("RETURNING TO MAIN MENU")
                DISPLAYSURF = pygame.display.set_mode((1000, 500))
                menucondition = True
                mazeinit = False
                mazemode = 'Custom'
                LocalMaze = []
                positions = []
                userpositions = []
                start = []
                end = []
                playerpos = []
                solved = False
                popupcustomcondition = False
                solved_by_user = False
                y_textfieldcase = False
                x_textfieldcase = False
                y_textfieldcolour = buttonmain
                x_textfieldcolour = buttonmain
                y_currentcolour = br
                y_buttontext = 'OK'
                x_currentcolour = br
                x_buttontext = 'OK'
                y_usertext = ''
                x_usertext = ''
                DISPLAYSURF.fill(br)
                DISPLAYSURF.blit(mazebr, (485,-5))
                DISPLAYSURF.blit(mazebr, (5,-5))
                menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
        
                menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
                
                selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
                
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)

                modetext = fontnormal.render(displaymode, True, colour5)
                modetextposition = modetext.get_rect()
                modetextposition.center = (80, 470)
                DISPLAYSURF.blit(modetext, modetextposition)
        else:
            currentbuttoncolourreturn = buttonmain

        # If otherwise clicked on either a button or text box:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK")

            # Make textbox white and make the input taking case true, ensuring the other one is coloured and set to false for inputs
            if y_textfield.collidepoint(cursor):
                y_textfieldcase = True
                x_textfieldcase = False
                y_textfieldcolour = colour5
                x_textfieldcolour = buttonmain 
                y_textfield = pygame.draw.rect(DISPLAYSURF, y_textfieldcolour, pygame.Rect(350, 215, 250, 35), 0, 20)
                y_usertext_rendered = fontnormal.render(y_usertext, True, (0,0,0))
                DISPLAYSURF.blit(y_usertext_rendered,(355,225))
                pygame.display.flip()

            # Make textbox white and make the input taking case true, ensuring the other one is coloured and set to false for inputs
            elif x_textfield.collidepoint(cursor):
                x_textfieldcase = True
                y_textfieldcase = False
                x_textfieldcolour = colour5
                y_textfieldcolour = buttonmain
                x_textfield = pygame.draw.rect(DISPLAYSURF, x_textfieldcolour, pygame.Rect(350, 335, 250, 35), 0, 20)
                x_usertext_rendered = fontnormal.render(x_usertext, True, (0,0,0))
                DISPLAYSURF.blit(x_usertext_rendered,(355,345))
                pygame.display.flip()
                
            # If button pressed and current textfield for that button isn't valid (input between 5 and 300 inclusive), make the button red with and exclamation mark. Otherwise, make it green with 'YAY'
            elif custom_y_button.collidepoint(cursor):
                print("OK: Y_CUSTOM")
                try:
                    int(y_usertext)
                    if int(y_usertext) > 300 or int(y_usertext) < 5:
                        raise ValueError
                except:
                    y_currentcolour = (255,0,0)
                    y_buttontext = '!'
                    errorcondition = True
                    custom_y_button = pygame.draw.rect(DISPLAYSURF, y_currentcolour, pygame.Rect(610, 215, 45, 35), 0, 20)
                    custom_y_text = fontnormal.render(y_buttontext, True, colour5)
                    custom_y_button_pos = custom_y_text.get_rect()
                    custom_y_button_pos.center = custom_y_button.center
                    DISPLAYSURF.blit(custom_y_text, custom_y_button_pos)
                else:
                    y_currentcolour = (0,200,0)
                    y_buttontext = 'YAY'
                    custom_y_button = pygame.draw.rect(DISPLAYSURF, y_currentcolour, pygame.Rect(610, 215, 45, 35), 0, 20)
                    custom_y_text = fontnormal.render(y_buttontext, True, colour5)
                    custom_y_button_pos = custom_y_text.get_rect()
                    custom_y_button_pos.center = custom_y_button.center
                    DISPLAYSURF.blit(custom_y_text, custom_y_button_pos)
                    y_passedcustom = True
                    pygame.display.flip()

                    
            # If button pressed and current textfield for that button isn't valid (int between 5 and 300 inclusive), make the button red with and exclamation mark. Otherwise, make it green with 'YAY'
            elif custom_x_button.collidepoint(cursor):
                print("OK: X_CUSTOM")
                try:
                    int(x_usertext)
                    if int(x_usertext) > 300 or int(x_usertext) < 5:
                        raise ValueError
                except:
                    x_currentcolour = (255,0,0)
                    x_buttontext = '!'
                    errorcondition = True
                    custom_x_button = pygame.draw.rect(DISPLAYSURF, x_currentcolour, pygame.Rect(610, 335, 45, 35), 0, 20)
                    custom_x_text = fontnormal.render(x_buttontext, True, colour5)
                    custom_x_button_pos = custom_x_text.get_rect()
                    custom_x_button_pos.center = custom_x_button.center
                    DISPLAYSURF.blit(custom_x_text, custom_x_button_pos)
                else:
                    x_currentcolour = (0,200,0)
                    x_buttontext = 'YAY'
                    custom_x_button = pygame.draw.rect(DISPLAYSURF, x_currentcolour, pygame.Rect(610, 335, 45, 35), 0, 20)
                    custom_x_text = fontnormal.render(x_buttontext, True, colour5)
                    custom_x_button_pos = custom_x_text.get_rect()
                    custom_x_button_pos.center = custom_x_button.center
                    DISPLAYSURF.blit(custom_x_text, custom_x_button_pos)
                    pygame.display.flip()
                    
                    x_passedcustom = True

        # If both inputs are valid, set up the display to be large enough for the new maze and instant generate a new maze based on the inputs
        if y_passedcustom and x_passedcustom:

            DISPLAYSURF = pygame.display.set_mode(((int(y_usertext)*10)+(2*mazeborder_x), (int(x_usertext)*10)+(2*mazeborder_y)))
            DISPLAYSURF.fill(br)
            pygame.display.flip()
            
            inputs = prim_maze_generation.initialize(int(y_usertext),int(x_usertext))
            LocalMaze = prim_maze_generation.generate_instant(inputs)

            # Display maze with squares ()
            for i in range (len(LocalMaze)):
                for j in range (len(LocalMaze[0])):
                    if LocalMaze[i][j] == 'w':
                        pygame.draw.rect(DISPLAYSURF, colour1, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
                    elif LocalMaze[i][j] == 'p':
                        pygame.draw.rect(DISPLAYSURF, br, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))

                pygame.display.flip()
                if inputs[4]:
                    break

            # Get ready for the game to be played
            exitmainmenu()
            mazemode = 'Custom'
            mazeinit = True
            popupcustomcondition = False
            menucondition = False
            y_textfieldcase = False
            x_textfieldcase = False
                


# Function for setting up the game
def exitmainmenu():
    global correctpositions
    global LocalMaze
    global DISPLAYSURF
    global menucondition
    global colour1
    global GreenPath
    global buttonmain
    global start
    global end
    global playerpos
    global mazeinit
    global usercolour
    global mazeborder_x
    global mazeborder_y
    global y_textfieldcase
    global x_textfieldcase
    global errorcondition
    global x_passedcustom
    global y_passedcustom
    global currentbuttoncolourreturn

    # Set vars to false just in case
    errorcondition = False
    x_passedcustom = False
    y_passedcustom = False
    
    DISPLAYSURF = pygame.display.set_mode(((len(LocalMaze[0]*10))+(2*mazeborder_x), (len(LocalMaze)*10)+(2*mazeborder_y)))
    DISPLAYSURF.fill(br)
    menucondition = False
    time.sleep(0.15)

    # Display maze for fixed presets
    for i in range (len(LocalMaze)):
        for j in range (len(LocalMaze[0])):
            if LocalMaze[i][j] == 'w':
                pygame.draw.rect(DISPLAYSURF, colour1, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
    
    pygame.display.flip()

    # Determine Start and End of the maze and make the user start at the start and add the user icon there. Add a green square at the end
    if not menucondition:
        for i in range (len(LocalMaze[0])):
            if LocalMaze[0][i] == 'p':
                start = [(i*10) + mazeborder_x, mazeborder_y]
                break
        print('STARTPOSE: ' + str(start))
        userpositions.append([start[0],start[1]])
        DISPLAYSURF.blit(userposicon, (start[0], start[1]))
        for i in range (len(LocalMaze[0])-1, 0, -1):
            if LocalMaze[len(LocalMaze)-1][i] == 'p':
                end = [(i*10) + mazeborder_x,((len(LocalMaze)-1)*10) + mazeborder_y]
                break

        print('ENDPOSE: ' + str(end))
        pygame.draw.rect(DISPLAYSURF, GreenPath, pygame.Rect(end[0], end[1], 10, 10))
        playerpos = start
        print('PLAYERPOSE: ' + str(playerpos))
        print(LocalMaze)

    # Execute maze_solver and save positions for calculating score
    correctpositions = maze_solver.ExecuteSolver(LocalMaze)

    # Init the box to display hot and cold
    init_tempbox = pygame.draw.rect(DISPLAYSURF, colour5,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 5, 10)
    init_temptext = fontnormal.render('Hot-Cold Off', True, colour5)
    init_temptextpos = init_temptext.get_rect()
    init_temptextpos.center = init_tempbox.center
    DISPLAYSURF.blit(init_temptext, init_temptextpos)
    
    pygame.display.flip()

# Takes care of buttons on the main menu
def menuautomation():
    global br
    global titlecolour
    global colour1
    global GreenPath
    global colour2
    global buttonmain
    global buttonhover
    global colour5
    global windowback
    global windowborder
    global DISPLAYSURF
    global width
    global height
    global menucondition
    global sliderpos
    global lightmode
    global clicks
    global LocalMaze
    global correctpositions
    global mazeinit
    global mazemode
    global usercolour
    global popupcustomcondition
    global currentbuttoncolourreturn
    global y_textfieldcolour
    global x_textfieldcolour
    global y_currentcolour
    global x_currentcolour
    global y_textfieldcase
    global x_textfieldcase
    global displaymode
    global instructioncase

    # Slider button click updates the colours and redisplays items to update colour scheme. Slider text is also changed based on mode, and so is the circle position
    if 50 <= cursor[0] <= 110 and 425 <= cursor[1] <= 455:
        if event.type == pygame.MOUSEBUTTONDOWN:
            lightmode = not lightmode
            print('THEME SLIDER CLICK: LIGHTMODE == ' + str(lightmode))
            if lightmode:
                sliderpos = 55
                br = (68,153,180)
                colour1 = (80,80,100)
                GreenPath = (93,255,50)
                colour2 = (5,225,75)
                buttonmain = (255, 75, 100)
                buttonhover = (255,160,185)
                colour5 = (217,215,221)
                windowback = (151,155,171)
                windowborder = (193,184,200)
                usercolour = (242,221,110)
                titlecolour = buttonmain
                y_textfieldcolour = buttonmain
                x_textfieldcolour = buttonmain
                y_currentcolour = br
                x_currentcolour = br
                DISPLAYSURF.fill(br)
                DISPLAYSURF.blit(mazebr, (485,-5))
                DISPLAYSURF.blit(mazebr, (5,-5))
                menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
            
                menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
                
                selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
            
                
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
              
                if y_textfieldcase:
                    y_textfield = pygame.draw.rect(DISPLAYSURF, y_textfieldcolour, pygame.Rect(350, 215, 250, 35), 0, 20)
                    pygame.display.flip()

                elif x_textfieldcase:
                    x_textfield = pygame.draw.rect(DISPLAYSURF, x_textfieldcolour, pygame.Rect(350, 335, 250, 35), 0, 20)
                    pygame.display.flip()
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
                displaymode = 'Light Mode'
                modetext = fontnormal.render(displaymode, True, colour5)
                modetextposition = modetext.get_rect()
                modetextposition.center = (80, 470)
                DISPLAYSURF.blit(modetext, modetextposition)
                if popupcustomcondition:
                    custombox_y = fontnormal.render('How tall do you want the maze (units)?', True, buttonmain)
                    custombox_y_pos = custombox_y.get_rect()
                    custombox_y_pos.center = (500, 190)
                    DISPLAYSURF.blit(custombox_y, custombox_y_pos)
            
                    custombox_x = fontnormal.render('How wide do you want the maze (units)?', True, buttonmain)
                    custombox_x_pos = custombox_x.get_rect()
                    custombox_x_pos.center = (500, 310)
                    DISPLAYSURF.blit(custombox_x, custombox_x_pos)
                    
            else:
                sliderpos = 85
                br = (30,30,30)
                colour1 = (80,80,100)
                GreenPath = (93,255,50)
                colour2 = (5,225,75)
                buttonmain = (19,150,225)
                buttonhover = (119,185,255)
                colour5 = (217,215,221)
                windowback = (61,65,81)
                windowborder = (93,94,110)
                usercolour = (242,221,110)
                titlecolour = buttonmain
                y_textfieldcolour = buttonmain
                x_textfieldcolour = buttonmain
                y_currentcolour = br
                x_currentcolour = br
                DISPLAYSURF.fill(br)
                DISPLAYSURF.blit(mazebr, (485,-5))
                DISPLAYSURF.blit(mazebr, (5,-5))
                menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
            
                menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
                
                selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
            
                
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
                if y_textfieldcase:
                    y_textfield = pygame.draw.rect(DISPLAYSURF, y_textfieldcolour, pygame.Rect(350, 215, 250, 35), 0, 20)
                    pygame.display.flip()

                elif x_textfieldcase:
                    x_textfield = pygame.draw.rect(DISPLAYSURF, x_textfieldcolour, pygame.Rect(350, 335, 250, 35), 0, 20)
                    pygame.display.flip()
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)
                displaymode = 'Dark Mode'
                modetext = fontnormal.render(displaymode, True, colour5)
                modetextposition = modetext.get_rect()
                modetextposition.center = (80, 470)
                DISPLAYSURF.blit(modetext, modetextposition)

                # If colour is changed while in the custom defining menu, readd the info text for text boxes
                if popupcustomcondition:
                    custombox_y = fontnormal.render('How tall do you want the maze (units)?', True, buttonmain)
                    custombox_y_pos = custombox_y.get_rect()
                    custombox_y_pos.center = (500, 190)
                    DISPLAYSURF.blit(custombox_y, custombox_y_pos)
            
                    custombox_x = fontnormal.render('How wide do you want the maze (units)?', True, buttonmain)
                    custombox_x_pos = custombox_x.get_rect()
                    custombox_x_pos.center = (500, 310)
                    DISPLAYSURF.blit(custombox_x, custombox_x_pos)

            # Delay to avoid random flickers and not staying in condition
            time.sleep(0.15)    
                

    # If not in the custom condition, check inputs for and display the How-To button and Maze Mode buttons, making them brighter when hovered on and executing commands and running exit functions when clicked, changing booleans and resetting when required, as well as displaying the parts for the popupcustom function if custom maze is clicked. The exitmainmenu function is run after the other presets, and also after having generated the specific maze for that preset using prim_maze_generation.generate(y, x). These mazes are also displayed to the screen. 
    if not popupcustomcondition:
        instruction = pygame.draw.rect(DISPLAYSURF, (242, 209, 61), pygame.Rect(800, 230, 160, 40), 0, 10)
        instructiontext = fontnormal.render('? How-To Play ?', True, (0, 0, 0))
        instructiontextpos = instructiontext.get_rect()
        instructiontextpos.center = instruction.center
        DISPLAYSURF.blit(instructiontext, instructiontextpos)

        if instruction.collidepoint(cursor):
            instruction = pygame.draw.rect(DISPLAYSURF, (247, 231, 156), pygame.Rect(800, 230, 160, 40), 0, 10)
            instructiontext = fontnormal.render('? How-To Play ?', True, (0, 0, 0))
            instructiontextpos = instructiontext.get_rect()
            instructiontextpos.center = instruction.center
            DISPLAYSURF.blit(instructiontext, instructiontextpos)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                instructioncase = True
                DISPLAYSURF.fill((255,255,255))
                DISPLAYSURF.blit(instructions, (162.5,30))
                pygame.display.flip()
            
        
      
        if 350 <= cursor[0] <= 650 and 170 <= cursor[1] <= 210:
            buttoneasy = pygame.draw.rect(DISPLAYSURF, buttonhover, pygame.Rect(500-(300/2), 170, 300, 40), 0, 10)
            easytext = fontnormal.render('Easy Maze', True, colour5)
            easyposition = easytext.get_rect()
            easyposition.center = buttoneasy.center
            DISPLAYSURF.blit(easytext, easyposition)
            if event.type == pygame.MOUSEBUTTONDOWN and LocalMaze == []:
                DISPLAYSURF = pygame.display.set_mode(((300)+(2*mazeborder_x), (300)+(2*mazeborder_y)))
                DISPLAYSURF.fill(br)
                pygame.display.flip()
                
                inputs = prim_maze_generation.initialize(30,30)
                while True:
                    inputs = prim_maze_generation.generate(inputs)
                    LocalMaze = inputs[0]
                    for i in range (len(LocalMaze)):
                        for j in range (len(LocalMaze[0])):
                            if LocalMaze[i][j] == 'w':
                                pygame.draw.rect(DISPLAYSURF, colour1, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
                            elif LocalMaze[i][j] == 'p':
                                pygame.draw.rect(DISPLAYSURF, br, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
    
                    pygame.display.flip()
                    if inputs[4]:
                        break
                exitmainmenu()
                mazeinit = True
                mazemode = 'Easy'
              
        else:
            if menucondition:
                buttoneasy = pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(500-(300/2), 170, 300, 40), 0, 10)
                easytext = fontnormal.render('Easy Maze', True, colour5)
                easyposition = easytext.get_rect()
                easyposition.center = buttoneasy.center
                DISPLAYSURF.blit(easytext, easyposition)
    
    
      
        if 350 <= cursor[0] <= 650 and 230 <= cursor[1] <= 270 and menucondition:
            buttonmed = pygame.draw.rect(DISPLAYSURF, buttonhover, pygame.Rect(500-(300/2), 230, 300, 40), 0, 10)
            medtext = fontnormal.render('Moderate Maze', True, colour5)
            medposition = medtext.get_rect()
            medposition.center = buttonmed.center
            DISPLAYSURF.blit(medtext, medposition)
            if event.type == pygame.MOUSEBUTTONDOWN and LocalMaze == []:
                DISPLAYSURF = pygame.display.set_mode(((450)+(2*mazeborder_x), (450)+(2*mazeborder_y)))
                DISPLAYSURF.fill(br)
                pygame.display.flip()
                
                inputs = prim_maze_generation.initialize(45,45)
                while True:
                    inputs = prim_maze_generation.generate(inputs)
                    LocalMaze = inputs[0]
                    for i in range (len(LocalMaze)):
                        for j in range (len(LocalMaze[0])):
                            if LocalMaze[i][j] == 'w':
                                pygame.draw.rect(DISPLAYSURF, colour1, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
                            elif LocalMaze[i][j] == 'p':
                                pygame.draw.rect(DISPLAYSURF, br, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
    
                    pygame.display.flip()
                    if inputs[4]:
                        break
                exitmainmenu()
                mazeinit = True
                mazemode = 'Moderate'
              
        else:
            if menucondition:
                buttonmed = pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(500-(300/2), 230, 300, 40), 0, 10)
                medtext = fontnormal.render('Moderate Maze', True, colour5)
                medposition = medtext.get_rect()
                medposition.center = buttonmed.center
                DISPLAYSURF.blit(medtext, medposition)
    
    
    
        if 350 <= cursor[0] <= 650 and 290 <= cursor[1] <= 330 and menucondition:
            buttonhard = pygame.draw.rect(DISPLAYSURF, buttonhover, pygame.Rect(500-(300/2), 290, 300, 40), 0, 10)
            hardtext = fontnormal.render('Hard Maze', True, colour5)
            hardposition = hardtext.get_rect()
            hardposition.center = buttonhard.center
            DISPLAYSURF.blit(hardtext, hardposition)
            if event.type == pygame.MOUSEBUTTONDOWN and LocalMaze == []:
                pygame.display.set_mode(((700)+(2*mazeborder_x), (700)+(2*mazeborder_y)))
                DISPLAYSURF.fill(br)
                pygame.display.flip()
                
                inputs = prim_maze_generation.initialize(70,70)
                while True:
                    inputs = prim_maze_generation.generate(inputs)
                    LocalMaze = inputs[0]
                    for i in range (len(LocalMaze)):
                        for j in range (len(LocalMaze[0])):
                            if LocalMaze[i][j] == 'w':
                                pygame.draw.rect(DISPLAYSURF, colour1, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
                            elif LocalMaze[i][j] == 'p':
                                pygame.draw.rect(DISPLAYSURF, br, pygame.Rect(j*10 + mazeborder_x, i*10 + mazeborder_y, 10, 10))
    
                    pygame.display.flip()
                    if inputs[4]:
                        break
                exitmainmenu()
                mazeinit = True
                mazemode = 'Hard'
              
        else:
            if menucondition:
                buttonhard = pygame.draw.rect(DISPLAYSURF, buttonmain,       pygame.Rect(500-(300/2), 290, 300, 40), 0, 10)
                hardtext = fontnormal.render('Hard Maze', True, colour5)
                hardposition = hardtext.get_rect()
                hardposition.center = buttonhard.center
                DISPLAYSURF.blit(hardtext, hardposition)
    
    
      
        if 350 <= cursor[0] <= 650 and 350 <= cursor[1] <= 390 and menucondition:
            buttoncustom = pygame.draw.rect(DISPLAYSURF, buttonhover,      pygame.Rect(350, 350, 300, 40), 0, 10)
            customtext = fontnormal.render('Custom Maze', True, colour5)
            customposition = customtext.get_rect()
            customposition.center = buttoncustom.center
            DISPLAYSURF.blit(customtext, customposition)
            if event.type == pygame.MOUSEBUTTONDOWN and LocalMaze == []:
                DISPLAYSURF.fill(br)
                DISPLAYSURF.blit(mazebr, (485,-5))
                DISPLAYSURF.blit(mazebr, (5,-5))
                popupcustomcondition = True
                currentbuttoncolourreturn = buttonmain
                menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
        
                menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
                
                selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
            
                
                moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)

                modetext = fontnormal.render(displaymode, True, colour5)
                modetextposition = modetext.get_rect()
                modetextposition.center = (80, 470)
                DISPLAYSURF.blit(modetext, modetextposition)

                custombox_y = fontnormal.render('How tall do you want the maze (units)?', True, buttonmain)
                custombox_y_pos = custombox_y.get_rect()
                custombox_y_pos.center = (500, 190)
                DISPLAYSURF.blit(custombox_y, custombox_y_pos)
        
                custombox_x = fontnormal.render('How wide do you want the maze (units)?', True, buttonmain)
                custombox_x_pos = custombox_x.get_rect()
                custombox_x_pos.center = (500, 310)
                DISPLAYSURF.blit(custombox_x, custombox_x_pos)
                popupcustom()

              
        else:
            if menucondition:
                buttoncustom = pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(500-(300/2), 350, 300, 40), 0, 10)
                customtext = fontnormal.render('Custom Maze', True, colour5)
                customposition = customtext.get_rect()
                customposition.center = buttoncustom.center
                DISPLAYSURF.blit(customtext, customposition)
                
# Displays the title of the maze being (preset) + Maze only when the maze has not been autosolved or solved by user
def mazetitledisplay():
    global title
    global titlecolour
    global fontheading
    global DISPLAYSURF
    global mazemode
    global LocalMaze
    global mazeborder_x
    global mazeborder_y
    global buttonmain
    global colour5
    global solved_by_user
    global solved
    
    if not solved_by_user and not solved:
        title = fontheading.render(mazemode + ' Maze', True, titlecolour)
        textposition = title.get_rect()
        textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x), mazeborder_y/2)
        DISPLAYSURF.blit(title, textposition)
    
# Does the same thing as menuautomation, but for maze buttons like Toggle Hot-Cold, Return to Menu, and Autosolve Maze
def mazeautomation():
    global DISPLAYSURF
    global LocalMaze
    global mazeborder_x
    global mazeborder_y
    global buttonmain
    global buttonhover
    global colour5
    global GreenPath
    global mazeinit
    global menucondition
    global mazemode
    global positions
    global userpositions
    global start
    global end
    global playerpos
    global solved
    global popupcustomcondition
    global solved_by_user
    global y_textfieldcolour
    global x_textfieldcolour
    global y_currentcolour
    global y_buttontext
    global x_currentcolour
    global x_buttontext
    global y_usertext
    global x_usertext
    global hotcoldexecute

    # Lightenes return button when hovered on, and returns to the main menu if clicked on, while resetting lists, bools, and some modified variables. Menu basics are also displayed like the background, wallpaper, and rectangles for the menu
    if ((len(LocalMaze[0]*10))+(2*mazeborder_x))-((mazeborder_x/2)+80) <= cursor[0] <= ((len(LocalMaze[0]*10))+(2*mazeborder_x))-((mazeborder_x/2)+80)+160 and ((len(LocalMaze)*5))+(mazeborder_y-20) <= cursor[1] <= ((len(LocalMaze)*5))+(mazeborder_y-20)+40 and not menucondition:
        buttonreturn = pygame.draw.rect(DISPLAYSURF, buttonhover,       pygame.Rect(((len(LocalMaze[0]*10))+(2*mazeborder_x))-((mazeborder_x/2)+80), ((len(LocalMaze)*5))+(mazeborder_y-20), 160, 40), 0, 10)
        returntext = fontnormal.render('Return To Menu', True, colour5)
        returnposition = returntext.get_rect()
        returnposition.center = buttonreturn.center
        DISPLAYSURF.blit(returntext, returnposition)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("RETURNING TO MAIN MENU")
            DISPLAYSURF = pygame.display.set_mode((1000, 500))
            menucondition = True
            mazeinit = False
            mazemode = ''
            LocalMaze = []
            positions = []
            userpositions = []
            start = []
            end = []
            playerpos = []
            solved = False
            popupcustomcondition = False
            solved_by_user = False
            hotcoldexecute = False
            y_textfieldcolour = buttonmain
            x_textfieldcolour = buttonmain
            y_currentcolour = br
            y_buttontext = 'OK'
            x_currentcolour = br
            x_buttontext = 'OK'
            y_usertext = ''
            x_usertext = ''
            DISPLAYSURF.fill(br)
            DISPLAYSURF.blit(mazebr, (485,-5))
            DISPLAYSURF.blit(mazebr, (5,-5))
            menurectback = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(520/2), 55, 520, 395), 0, 25)
        
            menurect = pygame.draw.rect(DISPLAYSURF, windowback, pygame.Rect(500-(500/2), 65, 500, 375), 0, 20)
            
            selectorrect = pygame.draw.rect(DISPLAYSURF, windowborder, pygame.Rect(500-(350/2), 150, 350, 260), 0, 20)
        
            
            moderect = pygame.draw.rect(DISPLAYSURF, windowback,       pygame.Rect(15, 410, 130, 80), 0, 15)

            modetext = fontnormal.render(displaymode, True, colour5)
            modetextposition = modetext.get_rect()
            modetextposition.center = (80, 470)
            DISPLAYSURF.blit(modetext, modetextposition)
    
    else:
        buttonreturn = pygame.draw.rect(DISPLAYSURF, buttonmain,       pygame.Rect(((len(LocalMaze[0]*10))+(2*mazeborder_x))-((mazeborder_x/2)+80), ((len(LocalMaze)*5))+(mazeborder_y-20), 160, 40), 0, 10)
        returntext = fontnormal.render('Return To Menu', True, colour5)
        returnposition = returntext.get_rect()
        returnposition.center = buttonreturn.center
        DISPLAYSURF.blit(returntext, returnposition)

    # Lighten the maze solver button if hovered, and turn all correct paths green if clicked while keeping the button light
    if ((mazeborder_x/2)-80) <= cursor[0] <= ((mazeborder_x/2)+80) and ((len(LocalMaze)*5))+(mazeborder_y-20) <= cursor[1] <= ((len(LocalMaze)*5))+(mazeborder_y-20)+40 and not menucondition:
        buttonsolve = pygame.draw.rect(DISPLAYSURF, buttonhover,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-20), 160, 40), 0, 10)
        solvetext = fontnormal.render('Autosolve Maze', True, colour5)
        solveposition = solvetext.get_rect()
        solveposition.center = buttonsolve.center
        DISPLAYSURF.blit(solvetext, solveposition)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("SOLVING MAZE")
            for i in range (len(correctpositions)):
                pygame.draw.rect(DISPLAYSURF, GreenPath, pygame.Rect((correctpositions[i][0]*10) + mazeborder_x, (correctpositions[i][1]*10)+mazeborder_y, 10, 10))
            solved = True

            # If only the computer solved the maze, show that it escaped by changing the title and covering up the old one
            if solved and not solved_by_user:
                pygame.draw.rect(DISPLAYSURF, br,       pygame.Rect(0, 40, 999999, 40), 0, 10)
                title = fontheading.render('The computer escaped!', True, titlecolour)
                textposition = title.get_rect()
                textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x), mazeborder_y/2)
                DISPLAYSURF.blit(title, textposition)
            time.sleep(0.15)
                
    else:
        if LocalMaze != [] and not solved:
            buttonsolve = pygame.draw.rect(DISPLAYSURF, buttonmain,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-20), 160, 40), 0, 10)
            solvetext = fontnormal.render('Autosolve Maze', True, colour5)
            solveposition = solvetext.get_rect()
            solveposition.center = buttonsolve.center
            DISPLAYSURF.blit(solvetext, solveposition)

    # Lighten Toggle Hot-Cold if hobered, and enable the state if clicked, making the output panel say 'Move to Show'
    if ((mazeborder_x/2)-80) <= cursor[0] <= ((mazeborder_x/2)+80) and ((len(LocalMaze)*5))+(mazeborder_y+40) <= cursor[1] <= ((len(LocalMaze)*5))+(mazeborder_y+80) and not menucondition:
        buttonhotcold = pygame.draw.rect(DISPLAYSURF, buttonhover,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y+40), 160, 40), 0, 10)
        hotcoldtext = fontnormal.render('Toggle Hot-Cold', True, colour5)
        hotcoldpos = hotcoldtext.get_rect()
        hotcoldpos.center = buttonhotcold.center
        DISPLAYSURF.blit(hotcoldtext, hotcoldpos)
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(DISPLAYSURF, br,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 0, 10)
            init_tempbox = pygame.draw.rect(DISPLAYSURF, colour5,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 5, 10)
            init_temptext = fontnormal.render('Move to Show', True, colour5)
            init_temptextpos = init_temptext.get_rect()
            init_temptextpos.center = init_tempbox.center
            DISPLAYSURF.blit(init_temptext, init_temptextpos)
            pygame.display.flip()
          
            if hotcoldexecute == True:
                pygame.draw.rect(DISPLAYSURF, br,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 0, 10)
                init_tempbox = pygame.draw.rect(DISPLAYSURF, colour5,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 5, 10)
                init_temptext = fontnormal.render('Hot-Cold Off', True, colour5)
                init_temptextpos = init_temptext.get_rect()
                init_temptextpos.center = init_tempbox.center
                DISPLAYSURF.blit(init_temptext, init_temptextpos)
            
                pygame.display.flip()
            hotcoldexecute = not hotcoldexecute

            # Remonder that these delays are to avoid bounce
            time.sleep(0.15)
                
    else:
        if not menucondition:
            buttonhotcold = pygame.draw.rect(DISPLAYSURF, buttonmain,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y+40), 160, 40), 0, 10)
            hotcoldtext = fontnormal.render('Toggle Hot-Cold', True, colour5)
            hotcoldpos = hotcoldtext.get_rect()
            hotcoldpos.center = buttonhotcold.center
            DISPLAYSURF.blit(hotcoldtext, hotcoldpos)

# This function takes in user movement inputs to move the userposition around the maze to get to the goal. If they are at the goal, the score will be calculated and displayed, as well as saved and sorted in the preset's score list and the game will tell you what your current solve ranked
def mazemaneuvering():
    global pastpos
    global playerpos
    global LocalMaze
    global DISPLAYSURF
    global titlecolour
    global buttonmain
    global GreenPath
    global usercolour
    global mazeborder_x
    global mazeborder_y
    global userpositions
    global solved_by_user
    global current_seconds
    global current_minutes
    global correctpositions
    global windowback
    global hotcoldexecute
    global easy_scores_list
    global moderate_scores_list
    global hard_scores_list
    global custom_scores_list
    
    press = pygame.key.get_pressed()

    # If the key pressed is a valid movement key (WASD or Up, Down, Left, Right) and the position in that direction is within the maze and not a wall: move there and update the current position
    if press[pygame.K_RIGHT] or press[pygame.K_UP] or press[pygame.K_LEFT] or press[pygame.K_DOWN] or press[pygame.K_w] or press[pygame.K_s] or press[pygame.K_a] or press[pygame.K_d]:
        pastpos = playerpos
        pygame.draw.rect(DISPLAYSURF, buttonmain, pygame.Rect(pastpos[0], pastpos[1], 10, 10))
        
        if (press[pygame.K_RIGHT] or press[pygame.K_d]) and playerpos[0] < ((len(LocalMaze[0])-1)*10+mazeborder_x) and LocalMaze[int(((playerpos[1])-mazeborder_y)/10)][int((playerpos[0]-(mazeborder_x-10))/10)] != 'w' and playerpos != end:
            print("RIGHTARROW")
            playerpos[0] += 10
    
        elif (press[pygame.K_LEFT] or press[pygame.K_a]) and playerpos[0] > mazeborder_x+10 and LocalMaze[int(((playerpos[1])-mazeborder_y)/10)][int((playerpos[0]-(mazeborder_x+10))/10)] != 'w' and playerpos != end:
            print("LEFTARROW")
            playerpos[0] -= 10
    
        elif (press[pygame.K_UP] or press[pygame.K_w]) and playerpos[1] > mazeborder_y+10 and LocalMaze[int((playerpos[1]-(mazeborder_y+10))/10)][int(((playerpos[0])-mazeborder_x)/10)] != 'w' and playerpos != end:
          print("UPARROW")  
          playerpos[1] -= 10
    
        elif (press[pygame.K_DOWN] or press[pygame.K_s]) and playerpos[1] < ((len(LocalMaze)-1)*10+mazeborder_y) and LocalMaze[int((playerpos[1]-(mazeborder_y-10))/10)][int(((playerpos[0])-mazeborder_x)/10)] != 'w' and playerpos != end:
            print("DOWNARROW")
            playerpos[1] += 10

        userpositions.append([playerpos[0],playerpos[1]])

        print('PLAYERPOSE: ' + str(playerpos))

        # Saves current position as grid coordinate ot be referred to when checking if user is hot/cold
        tempchecklist = [int((playerpos[0]-mazeborder_x)/10), int((playerpos[1]-mazeborder_y)/10)]

        print(tempchecklist)

        # If tempchecklist is one of the correct positions, output 'Hot' on the display panel with an orange background for the Hot-Cold display. Otherwise put out 'Cold' with a light teal background
        if tempchecklist in correctpositions:
            tempcase = 'Hot'
            tempcolour = (252, 127, 3)
            temptextcolour = colour5
        else:
            tempcase = 'Cold'
            tempcolour = (175, 240, 238)
            temptextcolour = (0, 0, 0)

        # Update userposition on screen
        DISPLAYSURF.blit(userposicon, (playerpos[0], playerpos[1]))

        if hotcoldexecute:
            tempbox = pygame.draw.rect(DISPLAYSURF, tempcolour,       pygame.Rect(((mazeborder_x/2)-80), ((len(LocalMaze)*5))+(mazeborder_y-80), 160, 40), 0, 10)
            temptext = fontnormal.render(tempcase, True, temptextcolour)
            temptextpos = temptext.get_rect()
            temptextpos.center = tempbox.center
            DISPLAYSURF.blit(temptext, temptextpos) 
            pygame.display.flip()

        # Calculate score by dividing length of correctpositions by lenght of userpositions (including wall hits as they are still moves) and multiplying by 100 (percentage). Depending on the mazemode, save the score to the designated list and sort from greatest to least to determine placement, outputting ranking for anything but a high score, and a 'HIGH SCORE!' message under the maze for a new high score
        if playerpos == end and not solved_by_user:
            print('USERPOSITIONS: ' + str(userpositions) + ', NUM OF POSITIONS: ' + str(len(userpositions)))
            for i in range (len(userpositions)):
                pygame.draw.rect(DISPLAYSURF, titlecolour, pygame.Rect(userpositions[i][0], userpositions[i][1], 10, 10))
                percentage = (len(correctpositions)/len(userpositions))*100
            
            if mazemode == 'Easy':
                easy_scores_list.append(percentage)
                easy_scores_list.sort(reverse = True)
                print(easy_scores_list)
                place = easy_scores_list.index(percentage) + 1
                if place == 1:
                    title = fontheading.render('HIGH SCORE!', True, (230, 209, 55))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)
                else:
                    title = fontheading.render('This was your #'+str(place)+' highest score.', True, (175, 232, 209))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)
              
            elif mazemode == 'Moderate':
                moderate_scores_list.append(percentage)
                moderate_scores_list.sort(reverse = True)
                print(moderate_scores_list)
                place = moderate_scores_list.index(percentage) + 1
                if place == 1:
                    title = fontheading.render('HIGH SCORE!', True, (230, 209, 55))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)
                else:
                    title = fontheading.render('This was your #'+str(place)+' highest score.', True, (175, 232, 209))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)

            elif mazemode == 'Hard':
                hard_scores_list.append(percentage)
                hard_scores_list.sort(reverse = True)
                print(hard_scores_list)
                place = hard_scores_list.index(percentage) + 1
                if place == 1:
                    title = fontheading.render('HIGH SCORE!', True, (230, 209, 55))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)
                else:
                    title = fontheading.render('This was your #'+str(place)+' highest score.', True, (175, 232, 209))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)

            else:
                custom_scores_list.append(percentage)
                custom_scores_list.sort(reverse = True)
                print(custom_scores_list)
                place = custom_scores_list.index(percentage) + 1
                if place == 1:
                    title = fontheading.render('HIGH SCORE!', True, (230, 209, 55))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)
                else:
                    title = fontheading.render('This was your #'+str(place)+' highest score.', True, (175, 232, 209))
                    textposition = title.get_rect()
                    textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x),(len(LocalMaze*10))+(mazeborder_y*1.5)-22.5)
                    DISPLAYSURF.blit(title, textposition)

            # If percentage is greater than 80, output it green in the top left, if it is between 80 and 40, output it yellow, and if it is lower than that, output it red. Floor the percentage and output with '% successful'
            if percentage > 80:
                percentage_colour = (175, 250, 195)

            elif percentage < 80 and percentage > 40:
                percentage_colour = (235, 206, 113)

            else:
                percentage_colour = (222, 40, 40)
          
            title = fontnormal.render(str(int(percentage)) + '% successful', True, percentage_colour)
            DISPLAYSURF.blit(title, (10, 10))
            
            
            solved_by_user = True
            pygame.draw.rect(DISPLAYSURF, br,       pygame.Rect(0, 40, 999999, 40), 0, 10)

            # Title that says that the user escaped, covering up the previous
            title = fontheading.render('You escaped!', True, titlecolour)
            textposition = title.get_rect()
            textposition.center = ((len(LocalMaze[0]*5))+(mazeborder_x), mazeborder_y/2)
            DISPLAYSURF.blit(title, textposition)
              
        time.sleep(0.25)


while True:
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

        # Management of textbox inputs for activated text box
        elif event.type == pygame.KEYDOWN:
            keypress = True
            if y_textfieldcase:
                print("Y_TEXTFIELD ADD ATTEMPT")
                if event.key == pygame.K_BACKSPACE:
                    y_usertext = y_usertext[:-1]
                    
                else:
                    if len(y_usertext) < 25:
                        y_usertext += event.unicode

                y_textfield = pygame.draw.rect(DISPLAYSURF, y_textfieldcolour, pygame.Rect(350, 215, 250, 35), 0, 20)
                y_usertext_rendered = fontnormal.render(y_usertext, True, (0,0,0))
                DISPLAYSURF.blit(y_usertext_rendered,(355,225))
                pygame.display.flip()
            
            if x_textfieldcase:
                print("X_TEXTFIELD ADD ATTEMPT")
                if event.key == pygame.K_BACKSPACE:
                    x_usertext = x_usertext[:-1]
                    print(x_usertext)
                    
                else:
                    if len(x_usertext) < 25:
                        x_usertext += event.unicode
                x_textfield = pygame.draw.rect(DISPLAYSURF, x_textfieldcolour, pygame.Rect(350, 335, 250, 35), 0, 20)
                x_usertext_rendered = fontnormal.render(x_usertext, True, (0,0,0))
                DISPLAYSURF.blit(x_usertext_rendered,(355,345))
                pygame.display.flip()
                        
        else:
            keypress = False
          
    cursor = pygame.mouse.get_pos()

    # Functions executed in the main loop
    if menucondition and not instructioncase:
        menudisplay()
        menuautomation()
        popupcustom()

    if mazeinit:
        mazetitledisplay()
        mazeautomation()
        if playerpos != end:
            mazemaneuvering()

    if instructioncase:
        instructionmenu()
  
    pygame.display.update()
