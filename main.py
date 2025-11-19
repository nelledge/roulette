import pygame
import sys

from funktions import *

pygame.init()
screen = pygame.display.set_mode((1, 1))  

# Immages 
background = pygame.image.load("pictures/roulette_simple_text.jpg").convert_alpha()
background = pygame.transform.scale(background, 
                                   (background.get_width()/6,
                                    background.get_height()/6))

# Backround
img_w = background.get_width()
img_h = background.get_height()
screen = pygame.display.set_mode((img_w,  img_h ))

# Colors
WHITE = (255, 255, 255)
GREEN_BACKROUND = (31, 146, 17)
DARK_GREEN = (42, 94, 36)
DARKGRAY = (120, 120, 120)
GREEN = (0, 200, 0)
LIGHT_GREEN = (59, 217, 66)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (199, 21, 8) 

# fonts
fonts_outside = pygame.font.SysFont(None, 40)

#Chip Fariablen 
# x , y , 1 Color , 2 Color , True or False if Clicked
blue_chip_coordinates_color = [200, 650, BLUE, WHITE, False]
red_chip_coordinates_color = [290, 650, RED, WHITE, False]
green_chip_coordinates_color = [380, 650, LIGHT_GREEN, WHITE, False]
black_chip_coordinates_color = [470, 650, BLACK, WHITE, False]

chip_radius = 15          
# button_text = 'Click Me!'

def main():
    running = True

    manque = pygame.Rect(481, 500, 150, 50)
    passe = pygame.Rect(490, 170, 120, 50)
    impair = pygame.Rect(320, 500, 150, 50)
    pair =  pygame.Rect(320, 170, 120, 50)

    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0,0))

        #Drawing the objekts
        draw_chips(blue_chip_coordinates_color, chip_radius, screen)
        draw_chips(red_chip_coordinates_color, chip_radius, screen)
        draw_chips(green_chip_coordinates_color, chip_radius, screen)
        draw_chips(black_chip_coordinates_color, chip_radius, screen)

        # draw_rect_with_text(manque, "Manque", mouse_pos)
        # draw_rect_with_text(passe, "Passe", mouse_pos)
        # draw_rect_with_text(impair, "Impair", mouse_pos)
        # draw_rect_with_text(pair, "Pair", mouse_pos)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if manque.collidepoint(mouse_pos):
                    print("Button 1 clicked!")

                mouse_x, mouse_y = event.pos

                if distens_to_sircle(blue_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Blue Chip clicked!')
                    blue_chip_coordinates_color[4] = checking_true_fals_chip(blue_chip_coordinates_color)

                if distens_to_sircle(red_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Red Chip clicked!')
                    red_chip_coordinates_color[4] = checking_true_fals_chip(red_chip_coordinates_color)
                
                if distens_to_sircle(green_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Red Chip clicked!')
                    green_chip_coordinates_color[4] = checking_true_fals_chip(green_chip_coordinates_color)
                
                if distens_to_sircle(black_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Red Chip clicked!')
                    black_chip_coordinates_color[4] = checking_true_fals_chip(black_chip_coordinates_color)
        
        #Displaying everthing at the end
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
