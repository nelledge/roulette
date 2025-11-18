import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1, 1))  

background = pygame.image.load("pictures/roulette_simple.jpg").convert_alpha()
background = pygame.transform.scale(background, 
                                   (background.get_width()/6,
                                    background.get_height()/6))

img_w = background.get_width()
img_h = background.get_height()
screen = pygame.display.set_mode((img_w,  img_h ))

# Colors
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARKGRAY = (120, 120, 120)
GREEN = (0, 200, 0)

# Font
font = pygame.font.SysFont(None, 40)

def draw_button(rect, text, mouse_pos):
    # Hover effect
    if rect.collidepoint(mouse_pos):
        color = DARKGRAY
    else:
        color = GRAY

    pygame.draw.rect(screen, color, rect, border_radius=8)

    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.x + 20, rect.y + 10))

def main():
    running = True

    inside_betts = pygame.Rect(100, 50, 200, 60)
    outsise_betts = pygame.Rect(400, 50, 200, 60)


    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0,0))

        draw_button(inside_betts, "Inside Betts", mouse_pos)
        draw_button(outsise_betts, "Outsise Betts", mouse_pos)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse_pos):
                    print("Button 1 clicked!")

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
