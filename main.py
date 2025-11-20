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
GREEN = (0, 200, 0)
LIGHT_GREEN = (59, 217, 66)

DARK_GRAY = (120, 120, 120)
GRAY = (99, 95, 82)

BLUE = (0, 0, 255)

BLACK = (0, 0, 0)

RED = (199, 21, 8)
RED_GRAY = (201, 75, 75) 

# fonts
fonts_outside = pygame.font.SysFont(None, 40)

#Chip Fariablen 
"""
0 --> x 
1 --> y 
2 --> 1 Color 
3 --> 2 Color 
4 --> True or False if Clicked
5 --> radius
6 --> Value of chip
"""

blue_chip_coordinates_color = [200, 650, BLUE, WHITE, False, 15, 5]
red_chip_coordinates_color = [290, 650, RED_GRAY, WHITE, False, 15, 10]
green_chip_coordinates_color = [380, 650, LIGHT_GREEN, WHITE, False, 15, 20]
black_chip_coordinates_color = [470, 650, GRAY, WHITE, False, 15, 50]

chip_radius = 15          
# button_text = 'Click Me!'
list_of_placed_cips = []

def main():
    betting_amount = 0

    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0,0))

        #Drawing the Chips
        draw_chips(blue_chip_coordinates_color)
        draw_chips(red_chip_coordinates_color)
        draw_chips(green_chip_coordinates_color)
        draw_chips(black_chip_coordinates_color)

        drawing_chips_on_square_outside(list_of_placed_cips) 

        showing_betting_amount(betting_amount) 

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos

                if distens_to_sircle(blue_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Blue Chip clicked!')
                    blue_chip_coordinates_color[4] = checking_true_fals_chip(blue_chip_coordinates_color)
                    color_pushed = blue_chip_coordinates_color
                    red_chip_coordinates_color[4] = False
                    green_chip_coordinates_color[4] = False
                    black_chip_coordinates_color[4] = False

                elif distens_to_sircle(red_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Red Chip clicked!')
                    red_chip_coordinates_color[4] = checking_true_fals_chip(red_chip_coordinates_color)
                    color_pushed = red_chip_coordinates_color
                    blue_chip_coordinates_color[4] = False
                    green_chip_coordinates_color[4] = False
                    black_chip_coordinates_color[4] = False

                
                elif distens_to_sircle(green_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Green Chip clicked!')
                    green_chip_coordinates_color[4] = checking_true_fals_chip(green_chip_coordinates_color)
                    color_pushed = green_chip_coordinates_color
                    blue_chip_coordinates_color[4] = False
                    red_chip_coordinates_color[4] = False
                    black_chip_coordinates_color[4] = False

                
                elif distens_to_sircle(black_chip_coordinates_color, mouse_x, mouse_y) <= chip_radius:
                    print('Black Chip clicked!')
                    black_chip_coordinates_color[4] = checking_true_fals_chip(black_chip_coordinates_color)
                    color_pushed = black_chip_coordinates_color
                    blue_chip_coordinates_color[4] = False
                    red_chip_coordinates_color[4] = False
                    green_chip_coordinates_color[4] = False



                for i, rect in enumerate(drawing_sqaures_outside()):
                    if rect.collidepoint(event.pos):

                        mouse_placment = (mouse_x, mouse_y, color_pushed) 
                        list_of_placed_cips.append(mouse_placment)

                        print(f"Square {i+1} clicked!")
                        print(mouse_placment)

                        betting_amount += color_pushed[6]

                        # Resetting all the chip colors 
                        blue_chip_coordinates_color[4] = False
                        red_chip_coordinates_color[4] = False
                        green_chip_coordinates_color[4] = False
                        black_chip_coordinates_color[4] = False

        #Displaying everthing at the end
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
