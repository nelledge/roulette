import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Test")

# Colors
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARKGRAY = (120, 120, 120)
GREEN = (0, 200, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Button function
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

    # Button rectangles
    button1 = pygame.Rect(50, 100, 200, 60)
    button2 = pygame.Rect(350, 100, 200, 60)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((50, 50, 50))

        # Draw buttons
        draw_button(button1, "Button 1", mouse_pos)
        draw_button(button2, "Button 2", mouse_pos)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(mouse_pos):
                    print("Button 1 clicked!")
                if button2.collidepoint(mouse_pos):
                    print("Button 2 clicked!")

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
