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
GREEN_BACKROUND = (31, 146, 17)
DARK_GREEN = (42, 94, 36)
DARKGRAY = (120, 120, 120)
GREEN = (0, 200, 0)

# Font
font = pygame.font.SysFont(None, 40)

def draw_button(rect, text, mouse_pos):
    # Hover effect
    if rect.collidepoint(mouse_pos):
        color = DARK_GREEN
    else:
        color = GREEN_BACKROUND

    pygame.draw.rect(screen, color, rect, border_radius=8)

    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.x + 20, rect.y + 10))

def main():
    running = True

    manque = pygame.Rect(481, 500, 150, 50)
    passe = pygame.Rect(490, 170, 120, 50)
    impair = pygame.Rect(320, 500, 150, 50)
    pair =  pygame.Rect(320, 170, 120, 50)


    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0,0))

        draw_button(manque, "Manque", mouse_pos)
        draw_button(passe, "Passe", mouse_pos)
        draw_button(impair, "Impair", mouse_pos)
        draw_button(pair, "Pair", mouse_pos)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if manque.collidepoint(mouse_pos):
                    print("Button 1 clicked!")

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
