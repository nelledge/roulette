import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

mario_img = pygame.image.load("pictures/mario.png").convert_alpha() #convert_ala gets ride of backround
mario_img = pygame.transform.scale(mario_img, 
                                   (mario_img.get_width()/4,
                                   mario_img.get_height()/4))

running = True

x = 0
clock = pygame.time.Clock()

delta_time = 0.1

while running:
    screen.fill((0,255,0))

    screen.blit(mario_img,(x, 30))
    screen.blit(mario_img, (x, 200))

    x += 50 * delta_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()