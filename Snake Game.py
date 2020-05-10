"""
Created on Sat May  9 23:33:35 2020

Title: Snake Game

@author: mr._white_hat_
"""

import sys
import time
import pygame
import random
import winsound

pygame.init()

display_width = 800
display_height = 600
snake_block = 10
snake_speed = 15

frequency = 2500
duration = 100

display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption('Snake Game by mr._white_hat_')

blue = (50, 153, 213)
black = (0, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
red = (255, 0, 0)
cream = (255, 253, 208)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('comicsansms', 25)
score_style = pygame.font.SysFont('bahnschrift', 35)

appleimg = pygame.image.load('apple.png')

def our_snake(snake_block, snake_list):
    for p in snake_list:
        pygame.draw.rect(display, brown, [p[0], p[1], snake_block, snake_block])
        
def Your_score(score):
    Score = score_style.render("Your Score: " + str(score), True, black)
    display.blit(Score, [10, 10])

def message(msg, color):
    Msg = font_style.render(msg, True, color)
    display.blit(Msg, [display_width /6 + 25, display_height /3 + 75])

def game_loop():
    game_over = False
    game_close = False

    x = display_width /2
    y = display_height /2
    
    x_change = 0
    y_change = 0
    
    snake_list = []
    snake_length = 1
    
    food_x = round(random.randrange(0, display_width -snake_block) /10.0) *10.0
    food_y = round(random.randrange(0, display_height -snake_block) /10.0) *10.0
    
    while not game_over:
        
        while game_close == True:
            time.sleep(1)
            display.fill(cream)
            message("You Lost!!! Press Q-Quit or C-Play Again", red)
            Your_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                    
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        
        display.fill(cream)
        display.blit(appleimg, (food_x, food_y))
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for p in snake_list[:-1]:
            if p == snake_head:
                game_close = True
                
        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)
        
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, display_width -snake_block) /10.0) *10.0
            food_y = round(random.randrange(0, display_height -snake_block) /10.0) *10.0
            winsound.Beep(frequency, duration)
            snake_length += 1
        
        clock.tick(snake_speed)
        
    pygame.quit()
    sys.exit()
    
game_loop()