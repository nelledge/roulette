import pygame, sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

image = pygame.image.load("pictures/wheel.png").convert_alpha()

angle = 0
center_pos = (WIDTH // 2, HEIGHT // 2)

running = True
while running:


    # Rotate
    angle += 2
    rotated = pygame.transform.rotate(image, angle)

    # Always center it
    rect = rotated.get_rect(center=center_pos)

    # Draw
    screen.fill((25, 25, 25))
    screen.blit(rotated, rect)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Check if mouse is on rotated image rect
            if rect.collidepoint(mouse_pos):

                # Convert click coordinates to the rotated surface
                lx = mouse_pos[0] - rect.x
                ly = mouse_pos[1] - rect.y

                if 0 <= lx < rotated.get_width() and 0 <= ly < rotated.get_height():
                    alpha = rotated.get_at((lx, ly)).a
                    if alpha > 0:
                        print("Wheel clicked!")
