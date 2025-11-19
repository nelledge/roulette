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

    # Draw number 50 in the center
    font = pygame.font.SysFont(None, 30)  # 40 = font size, adjust as you like

    text_chip = str(entety[6]) #Turning int into sring because pygame needs that, for some reson :| 
    text = font.render(text_chip, True, WHITE)  # white text

    text_rect = text.get_rect(center=center)
    screen.blit(text, text_rect)

    # If entety[4] is True, also draw squares outside
    if entety[4] == True:
        drawing_sqaures_outside()


def changing_chip_outside_square(list_of_placed_cips): 
    # list_of_placed_cips has the x, y and the entety of the last pushed chip

    for x, y, color in list_of_placed_cips:
        pygame.draw.circle(screen, color[2], (x, y), color[5])


def drawing_sqaures_outside():
        outside_x = [193, 365, 530]  
        outside_y = [177, 506]  

        x_square = 40
        y_square = 40

        squares = [] 

        for y in outside_y:          
            for x in outside_x:      
                points = pygame.Surface((x_square, y_square), pygame.SRCALPHA)
                points.fill((0, 0, 255, 128))
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

