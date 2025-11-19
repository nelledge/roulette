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

def draw_chips(entety, radius, sreen_input):
    center = (entety[0], entety[1])
    if entety[4] == False:
        colur = entety[2]
        pygame.draw.circle(screen, colur, center, radius)
    else:
        colur = entety[3]
        pygame.draw.circle(screen, colur, center, radius)
        drawing_sqaures_outside()


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

