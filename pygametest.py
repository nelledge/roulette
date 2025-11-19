# import pygame

# pygame.init()

# screen = pygame.display.set_mode((640, 640))

# mario_img = pygame.image.load("pictures/mario.png").convert_alpha() #convert_ala gets ride of backround
# mario_img = pygame.transform.scale(mario_img, 
#                                    (mario_img.get_width()/4,
#                                    mario_img.get_height()/4))

# running = True

# x = 0
# clock = pygame.time.Clock()

# delta_time = 0.1

# while running:
#     screen.fill((0,255,0))

#     screen.blit(mario_img,(x, 30))
#     screen.blit(mario_img, (x, 200))

#     x += 50 * delta_time
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circular Button Click Example')

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Circular button properties
button_center = (400, 300)  # Center of the button
button_radius = 50           # Radius of the button
button_text = 'Click Me!'

# Function to draw the circular button
def draw_button():
    pygame.draw.circle(screen, BLUE, button_center, button_radius)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(button_text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_center)
    screen.blit(text_surface, text_rect)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the circular button
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - button_center[0]) ** 2 + (mouse_y - button_center[1]) ** 2) ** 0.5
            if distance <= button_radius:
                print('Button clicked!')

    # Fill background
    screen.fill(BLACK)

    # Draw button
    draw_button()

    # Update display
    pygame.display.flip()
