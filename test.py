import pygame
import sys
import math

pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load image (must have transparency)
image = pygame.image.load("pictures/wheel.png").convert_alpha()

# Start angle
angle = 0

# Center position where the image should rotate around
pos = (400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase rotation angle
    angle += 2  # degrees per frame

    # Rotate the image
    rotated = pygame.transform.rotate(image, angle)

    # Get a rect and center it at the desired position
    rect = rotated.get_rect(center=pos)

    # Draw
    # screen.fill((255, 255, 255))
    screen.blit(rotated, rect)

    pygame.display.update()
    clock.tick(60)
