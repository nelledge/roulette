import pygame

pygame.init()

screen = pygame.display.set_mode((1, 1))  

background = pygame.image.load("pictures/roulett.jpg").convert_alpha()
background = pygame.transform.scale(background, 
                                   (background.get_width()/4,
                                    background.get_height()/4))

img_w = background.get_width()
img_h = background.get_height()
screen = pygame.display.set_mode((img_w, img_h))

def main():
    running = True
    while running:
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
