import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
center = (250, 250)
size = 80

# Diamond shape
points = [
    (center[0], center[1] - size),
    (center[0] + size, center[1]),
    (center[0], center[1] + size),
    (center[0] - size, center[1])
]

running = True
while running:
    screen.fill((0,150,0))
    mouse = pygame.mouse.get_pos()

    shape = pygame.draw.polygon(screen, (200,0,0), points)

    if shape.collidepoint(mouse):
        pygame.draw.polygon(screen, (150,0,0), points)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN and shape.collidepoint(mouse):
            print("Diamond clicked!")

    pygame.display.flip()

pygame.quit()
