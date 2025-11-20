import pygame
from main import *

def draw_rect_with_text(rect, text, mouse_pos):
    # Hover effect
    if rect.collidepoint(mouse_pos):
        color = DARK_GREEN
    else:
        color = GREEN_BACKROUND

    pygame.draw.rect(screen, color, rect, border_radius=8)

    label = fonts_outside.render(text, True, WHITE)
    screen.blit(label, (rect.x + 20, rect.y + 10))

def draw_chips(entety):
    center = (entety[0], entety[1])
    radius = entety[5]

    # color depending on state
    if entety[4] == False:
        colur = entety[2]
    else:
        colur = entety[3]

    pygame.draw.circle(screen, colur, center, radius)

    font_chip = pygame.font.SysFont(None, 30)  

    text_chip = str(entety[6]) #Turning int into sring because pygame needs that, for some reson :| 
    text = font_chip.render(text_chip, True, WHITE)  

    text_rect = text.get_rect(center=center)
    screen.blit(text, text_rect)

    # If entety[4] is True, also draw squares outside
    if entety[4] == True:
        drawing_sqaures_outside()
        drawing_sqaures_inside()


def drawing_chips_on_square_outside(list_of_placed_cips): 
    # list_of_placed_cips has the x, y and the entety of the last pushed chip

    for x, y, color in list_of_placed_cips:
        pygame.draw.circle(screen, color[2], (x, y), color[5])

        font_chip = pygame.font.SysFont(None, 30)  

        text_chip = str(color[6]) #Turning int into sring because pygame needs that, for some reson :| 
        text = font_chip.render(text_chip, True, WHITE)  

        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def drawing_sqaures_outside():
        #for x, y = 40
        # outside_x = [193, 365, 530]  
        # outside_y = [177, 506]  

        #for x,y = 120
        outside_x = [160, 325, 495]  
        outside_y = [137, 467]  
        x_square_outside = 120
        y_square_outside = 120

        squares_outside = [] 

        for y in outside_y:          
            for x in outside_x:      
                points = pygame.Surface((x_square_outside, y_square_outside), pygame.SRCALPHA)
                points.fill((0, 0, 255, 50))
                screen.blit(points, (x, y))

                squares_outside.append(pygame.Rect(x, y, x_square_outside, y_square_outside))
        
        return squares_outside

def drawing_sqaures_inside():
        inside_x = [623, 580,537,494,451,406, 361, 320, 275, 230, 185, 145]
        inside_y = [290, 355, 420]
        x_square_inside = 15
        y_square_inside = 15
        
        squares_inside = [] 
        
        for x in inside_x:          
            for y in inside_y:      
                points = pygame.Surface((x_square_inside, y_square_inside), pygame.SRCALPHA)
                points.fill((0, 0, 255, 100))
                screen.blit(points, (x, y))

                squares_inside.append(pygame.Rect(x, y, x_square_inside, y_square_inside))
        
        return squares_inside

def distens_to_sircle (entety, mouse_x, mouse_y):
    distance = ((mouse_x - entety[0]) ** 2 + 
            (mouse_y - entety[1]) ** 2) ** 0.5
    return distance

def checking_true_fals_chip (entety):
    if entety[4] == False:
        return True
    else:
        return False

def showing_betting_amount (amount):
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render((f"{amount}€"), True, BLACK)
    screen.blit(text_surface, (50, 50))
