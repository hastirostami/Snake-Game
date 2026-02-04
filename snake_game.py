import pygame
import time
import random
pygame.init()
a = 800
b = 600
dis = pygame.display.set_mode((a, b))
pygame.display.set_caption("snake")
snake_block = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)
def message(msg):
    mesg = font_style.render(msg, True, (255, 0, 0))
    dis.blit(mesg, (a / 6, b /3))  # متن در وسط صفحه نمایش داده شود
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,(0,0,0),(x[0],x[1],snake_block,snake_block))
def game_loop():
    x1 = a / 2
    y1 = b / 2
    x1_change = 0
    y1_change = 0
    foodx=round(random.randrange(0,a-snake_block)/10)*10
    foody=round(random.randrange(0,b-snake_block)/10)*10
    snake_list=[]
    L_snake=1

    game_over = False
    game_close = False
    while not game_over:
        while game_close== True:
            dis.fill((50,153,213))
            message("you lose.press C-play again or Q-Quit")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over= True
                        game_close=False
                    if event.key==pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        x1 += x1_change
        y1 += y1_change
        if x1 >= a or x1 < 0 or y1 >= b or y1 < 0:
            game_close = True
        dis.fill((50, 153, 213))
        pygame.draw.rect(dis, (0, 0, 0), (x1, y1, snake_block, snake_block))
         
        
        pygame.draw.rect(dis,(0,255,0),(foodx,foody,snake_block,snake_block))
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>L_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close= True
        our_snake(snake_block,snake_list)
        if x1==foodx and y1==foody:
            L_snake+=1
            foodx=round(random.randrange(0,a-snake_block)/10)*10
            foody=round(random.randrange(0,b-snake_block)/10)*10
        
        pygame.display.update()
        clock.tick(30)


    message("You Lose")
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
game_loop()
