import pygame


screen_width = 800
screen_height = 600

black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)

    pygame.display.flip()

pygame.quit()