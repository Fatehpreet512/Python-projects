import pygame
import random
x=pygame.init()
#defining colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
#game window
game_window=pygame.display.set_mode((500,500))
pygame.display.set_caption('THE HUNGRY SNAKE')
clock=pygame.time.Clock()
#function to print on screen
font=pygame.font.Font(None, 55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text, [x,y])


#function to make snake
def plot(game_window,color,snk_list,size_x,size_y):
    for a,b in snk_list:
        pygame.draw.rect(game_window,color,[a,b,size_x,size_y])    

#Welcome page
def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(black)
        font=pygame.font.Font(None, 30)
        screen_text=font.render("Welcome to feed The Hungr Snake",True,green)
        game_window.blit(screen_text, [90,200])
        
        screen_text=font.render("Press Space to start the game",True,green)
        game_window.blit(screen_text, [110,230])

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               exit_game=True
               break


            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_SPACE:
                  gameloop()
        pygame.display.update()
        clock.tick(30)

#game loop
def gameloop():
    #game variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=10
   
    fps=30
    velocity_x=0
    velocity_y=0
    food_x=random.randint(0,500)
    food_y=random.randint(0,500)
    score=0
    
    snk_list=[]
    snk_size=1

    #HIGH SCORE
    

    with open('hiscore.txt','r') as f:
        highscore=f.read()

    while not exit_game :
        if game_over:
            if score>int(highscore):
                highscore=score

            with open('hiscore.txt','w') as f:
                 f.write(str(highscore))


            font=pygame.font.Font(None, 30)
            screen_text=font.render('Game Over,Press SPACE to Restart',True,red)
            game_window.blit(screen_text, [80,250])


            for event in pygame.event.get():


                if event.type==pygame.QUIT:
                    exit_game=True
                    break
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        gameloop()
                
        else:
            for event in pygame.event.get():


                if event.type==pygame.QUIT:
                    exit_game=True
                    break
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=10
                        velocity_x=0
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score=score+10
                food_x=random.randint(0,500)
                food_y=random.randint(0,500)
                snk_size+=5
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            game_window.fill(black)
            text_screen("SCORE:"+str(score),red,5,5)
            font=pygame.font.Font(None, 30)
            screen_text=font.render("HIGH SCORE:"+str(highscore),True,red)
            game_window.blit(screen_text, [320,5])

            
            
            head=[]

            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_size:
                del snk_list[0]
            plot(game_window,green,snk_list,snake_size,snake_size)
            
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

            if snake_x>500 or snake_x<0 or snake_y>500 or snake_y<0:
                game_over=True
        
            if head in snk_list[:-2]:
                game_over=True


        pygame.display.update()

        clock.tick(fps)
    pygame.quit()
    quit()

welcome()