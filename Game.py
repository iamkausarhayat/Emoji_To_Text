# import pygame
# import random
# pygame.init()

# #colours
# white =(255,255,255)
# red = (255,0,0)
# black =(0,0,0)

# #Creating Window
# screen_width = 900
# screen_height = 600
# gamewindow = pygame.display.set_mode((screen_width, screen_height ))

# # Game Title
# pygame.display.set_caption("Snake With Kausar Hayat Programer")
# pygame.display.update()

# #Game Specific Varibles
# exit_Game =False
# Gamd_Over = False
# snake_x = 45
# snake_y = 55
# velocity_x=0 
# velocity_y=0



# food_x = random.randint(20,screen_width)
# food_y = random.randint(20,screen_height)
# score  = 0
# snake_size =10
# fps = 60
# init_velocity = 5

# clock  = pygame.time.Clock()
# font =  pygame.font.SysFont(None,55)

# def text_Screen(text,colour,x,y):
#     screen_text = font.render(text,True,colour)
#     gamewindow.blit(screen_text,[x,y])

# def plot_snake(gameWindow, color, snk_list, snake_size):
#     for x,y in snk_list:
#         pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# snk_list = []
# snk_length = 1            
 
#  # Game Loop
# while not exit_Game:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit_Game = True

#         if event.type == pygame.KEYDOWN:
#             if event.key ==pygame.K_RIGHT:
#                 velocity_x =  init_velocity   
#                 velocity_y = 0

#             if event.key ==pygame.K_LEFT:
#                 velocity_x =  - init_velocity
#                 velocity_y = 0

#             if event.key ==pygame.K_UP:
#                 velocity_y =- init_velocity 
#                 velocity_x = 0

#             if event.key ==pygame.K_DOWN:
#                 velocity_y = init_velocity  
#                 velocity_x =0

#     snake_x = snake_x + velocity_x
#     snake_y = snake_y + velocity_y

#     if abs(snake_x -  food_x) < 10 and abs(snake_y - food_y) < 10:
#         score += 1
#         food_x = random.randint(0,screen_width)
#         food_y = random.randint(0,screen_height)
#         snk_length +=5

    
#     gamewindow.fill(white)
#     text_Screen("Score: " + str(score * 10), red, 5, 5)
#     pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])


#     head = []
#     head.append(snake_x)
#     head.append(snake_y)
#     snk_list.append(head)

#     if len(snk_list)>snk_length:
#         del snk_list[0]

#     # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
#     plot_snake(gamewindow, black, snk_list, snake_size)
#     pygame.display.update()
#     clock.tick(fps)

# pygame.quit
# quit()
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("Number is not prime")

