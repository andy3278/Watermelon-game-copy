import pygame
import math


screen_width = 600
screen_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green  = (0 , 255 , 0)

screen = pygame.display.set_mode((screen_width, screen_height))

# define scores of each ball
white_score = 10
red_score = 20
yellow_score = 30
green_score = 40

# define ball speed and redius
ball_speed = 1
white_radius = 8
red_radius = 11
yellow_radius = 16
green_radius = 20

box_bottom = 720 - white_radius 
box_left = 40 + white_radius
box_right = 560 - white_radius

balls = []

pygame.init()
running = True

while running:

    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # draw a white ball when mouse is clicked
            ball_y = event.pos[1]
            ball_x = event.pos[0]
            balls.append([ball_x, ball_y, ball_speed])
            
    
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            dx = balls[i][0] - balls[j][0]
            dy = balls[i][1] - balls[j][1]

            distance = math.sqrt(dx **2 + dy **2)
            if distance < 2 * white_radius:
                # update speed of both balls when they collide
                balls[i][2] *= -0.5
                balls[j][2] *= -0.5
            # bacasue downward in pygame is positive
        if balls[i][1] < box_bottom:
            balls[i][1] += balls[i][2]
        else:
            balls[i][1] = box_bottom
            balls[i][2] *= -0.5
        white_ball = pygame.draw.circle(screen, white, (balls[i][0], balls[i][1]), white_radius)
    # draw 3 lines to make a rectangle with upper side open
    pygame.draw.line(screen, white, (40, 40), (40, 720), 1)
    pygame.draw.line(screen, white, (40, 720), (560, 720), 1)
    pygame.draw.line(screen, white, (560, 720), (560, 40), 1)
    
    pygame.display.update()

pygame.quit()