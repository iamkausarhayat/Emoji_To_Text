# # # #print numbers from 1 to 100
# # # i = 100
# # # while i>=1:
# # #     print(i)
# # #     i -=1
# # #print the multiplication table of number n
# # n = int(input("Enter number for multiplication table of:"))
# # i =  1
# # while i<=10:
# #     print(n,"*",i,"=",n*i)
# #     i +=1
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx< len(nums):
#     print(nums[idx])
#     idx +=1
import pygame
import random
pygame.init()

#colours
white =(255,255,255)
red = (255,0,0)
black =(0,0,0)

screen_width = 900
screen_height = 600

#Creating Window
gamewindow = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption("Snake With Kausar Programer")
pygame.display.update()

#Game Specific Varibles
exit_Game =False
Gamd_Over = False
snake_x = 45
snake_y = 55
velocity_x=0 
velocity_y=0
score  = 0
food_x = random.randint(20,screen_width)
food_y = random.randint(20,screen_height)

snake_size =10
fps = 30
init_velocity = 5

clock  = pygame.time.Clock()
font =  pygame.font.SysFont(None,55)

def text_Screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gamewindow.blit(screen_text,[x,y])

def plot_snake (gamewindow,colour,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, colour,[x,y,snake_size,snake_size])



snake_list = []
snake_length = 1
 
while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                velocity_x =  init_velocity   
                velocity_y = 0
            if event.key ==pygame.K_LEFT:
                velocity_x =  - init_velocity
                velocity_y = 0
            if event.key ==pygame.K_UP:
                velocity_y =- init_velocity 
                velocity_x = 0
            if event.key ==pygame.K_DOWN:
                velocity_y = init_velocity  
                velocity_x =0           
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x -  food_x) < 7 and abs(snake_y - food_y) < 7:
        score += 10
        
        food_x = random.randint(20,screen_width)
        food_y = random.randint(20,screen_height)
        snake_length +=5

    gamewindow.fill(white)
    text_Screen("Score:"+str(score*10),red,5,5)
    pygame.draw.rect(gamewindow,red,[food_x , food_y, snake_size, snake_size])
     


    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

   # pygame.draw.rect(gamewindow, black,[snake_x, snake_y,snake_size,snake_size])
    plot_snake = (gamewindow,black,snake_list,snake_size)
    pygame.display.update()   
    clock.tick(fps)  

pygame.quit()
quit()