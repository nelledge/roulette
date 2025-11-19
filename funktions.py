import pygame
from main_visuel import *

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
    # font_chip = pygame.font.SysFont(None, 36)
    # text_surface = fonts_outside_chip.render(button_text, True, WHITE)
    # text_rect = text_surface.get_rect(center=center)
    # screen.blit(text_surface, text_rect)

def distens_to_sircle (entety, mouse_x, mouse_y):
    distance = ((mouse_x - entety[0]) ** 2 + 
            (mouse_y - entety[1]) ** 2) ** 0.5
    return distance

def checking_true_fals_chip (entety):
    if entety[4] == False:
        return True
    else:
        return False

