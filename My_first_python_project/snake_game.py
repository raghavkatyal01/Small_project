import pygame
pygame.init()
import random


# Background Color (using RGB values range(0,255) for diff colors)
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
 
#Creating Game  Window and set its length and breadth and tittle
screen_width=900
screen_height=600 

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock=pygame.time.Clock()       # here we define clock so that we should update the frame with time   

#DISPLAY THE TXT ON SCREEN(SCORE)
font=pygame.font.SysFont(None,55)

#File handling for high score

def text_screen(text,color,x,y):
    text_screen=font.render(text,True, color)      #IT TELLS  THE WHAT TEXT TO DISPLAY AND COLOR OF THAT  TEXT
    gameWindow.blit(text_screen,[x,y]) 

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])    # in list it contain position of coordinate in x,y and length,width of snake
# WELCOME SCREEN
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((223,229,230))
        text_screen("Welcome to snake game",black,200,180)
        text_screen("PRESS SPACE TO CONTINUE GAME",black,90,230)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()    
        pygame.display.update()
        clock.tick(40)                
# Creating a Game Loop
def gameloop():
    # Creating a Game variable
    game_over=False
    exit_game=False
    snake_x=45                  # Snake position in x axis 
    snake_y=55                  # Snake position in y axis    
    snake_size=10
    fps=30
    velocity_x=0
    velocity_y=0
    vel_init=5
    food_x=random.randint(20,screen_width/2)            # Here  we create the random int using random module by randit function(to plot snake food)
    food_y=random.randint(20,screen_height/2)
    # increasing the snake length
    snk_list=[]
    snk_length=1
    with open ("highscore.txt","r") as f:
        highscore = f.read()
    # NOW CREATING THE SCORE
    score = 0
    while  not  exit_game:
        if game_over:
            gameWindow.fill(black)
            text_screen("GAME OVER -- PRESS ENTER TO CONTINUE",red,40,250)
            with open ("highscore.txt","w") as f:
                f.write(str(highscore))
            for event in pygame.event.get():          
                    if event.type == pygame.QUIT:
                        exit_game=True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()    
        else:

            for event in pygame.event.get():          #(Event Handling) Here  we creating the event that is performed by the user in order to get desired result
                if event.type == pygame.QUIT: 
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel_init               # From  here i assign the velocity in snake  in particular direction
                        velocity_y =  0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -vel_init
                        velocity_y =  0
                    if event.key == pygame.K_UP:
                        velocity_y = -vel_init
                        velocity_x =  0       
                    if event.key == pygame.K_DOWN:
                        velocity_y = vel_init
                        velocity_x =  0    
            
            pygame.draw.rect(gameWindow,red,[snake_x,snake_y,snake_size,snake_size])    # in list it contain position in x,y and length,width of snake        

        # GIVING VELOCITY TO SNAKE
            snake_x+=velocity_x
            snake_y+=velocity_y
        # HERE WE COMPARE THE POSITION OF SNAKE AND FOOD IF DIST BTW THEM NEARLY EQUAL THEN SCORE WILL INCREASE
            if abs(snake_x-food_x) < 6 and  abs(snake_y-food_y) < 6:      
                score+=10
                snk_length+=5
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                if score > int(highscore):
                    highscore = score
            gameWindow.fill(white)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            text_screen("SCORE: "+str(score) + "    Highscore : "+str(highscore),red,5,5)

        #if we not create head initially the game will not start as snk_list is empty
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            #To CONTROL THE LENGTH OF SNAKE 
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True    

            if snake_x < 0 or snake_x > screen_width  or snake_y < 0 or snake_y > screen_height:
                game_over=True
                
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()  
        clock.tick(fps)    #(fps = frame per second)  
    pygame.quit()
    quit()
welcome()

