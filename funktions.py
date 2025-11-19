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

def draw_chips(center, radius, colur):
    pygame.draw.circle(screen, colur, center, radius)
    # font_chip = pygame.font.SysFont(None, 36)
    # text_surface = fonts_outside_chip.render(button_text, True, WHITE)
    # text_rect = text_surface.get_rect(center=center)
    # screen.blit(text_surface, text_rect)