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

        x_square = 120
        y_square = 120

        squares = [] 

        for y in outside_y:          
            for x in outside_x:      
                points = pygame.Surface((x_square, y_square), pygame.SRCALPHA)
                points.fill((0, 0, 255, 50))
                screen.blit(points, (x, y))

                squares.append(pygame.Rect(x, y, x_square, y_square))
        
        return squares

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
