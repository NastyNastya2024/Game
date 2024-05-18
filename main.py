import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pygame Game')
icon = pygame.image.load('img.jpg/kir2603_A_girl_with_long_chestnut_hair_and_big_grey_eyes_a_smal_c10c2635-aff8-4be7-8548-215d9802c3af.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img.jpg/target.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass



pygame.quit()