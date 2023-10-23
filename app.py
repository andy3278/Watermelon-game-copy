import pygame
import math


screen_width = 600
screen_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green  = (0 , 255 , 0)

color_order = [white, red, yellow, green]

screen = pygame.display.set_mode((screen_width, screen_height))

# define scores of each ball
white_score = 10
red_score = 20
yellow_score = 30
green_score = 40

score_order = [white_score, red_score, yellow_score, green_score]

# define ball speed and redius
ball_speed = 1
white_radius = 8
red_radius = 11
yellow_radius = 16
green_radius = 20

radius_order = [white_radius, red_radius, yellow_radius, green_radius]

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
            balls.append([ball_x, ball_y, ball_speed, white, white_radius])
            
    
    i = 0
    while i < len(balls):
        for j in range(i+1, len(balls)):
            dx = balls[i][0] - balls[j][0]
            dy = balls[i][1] - balls[j][1]

            distance = math.sqrt(dx **2 + dy **2)
            if distance < 2 * white_radius:
                # check if the balls are of same color
                if balls[i][3] == balls[j][3]:
                    color_index = color_order.index(balls[i][3])
                    if color_index + 1 < len(color_order):
                        # add a new ball with next color
                        balls.append([balls[i][0], balls[i][1], balls[i][2] , color_order[color_index + 1], radius_order[color_index + 1]])
                        # remove the balls of same color
                        balls.remove(balls[i])
                        balls.remove(balls[j])
                        # update index after remove
                        i -= 1
                        break
                    else:
                        # update speed of both balls when they collide
                        balls[i][2] *= -0.5
                        balls[j][2] *= -0.5
        i += 1
            # bacasue downward in pygame is positive
    for ball in balls:
        if ball[1] < 720 - ball[4]:
            ball[1] += ball[2]
        else:
            ball[1] = 720 - ball[4]
            ball[2] *= -0.5
        any_ball = pygame.draw.circle(screen, ball[3], (ball[0], ball[1]), ball[4])
    # draw 3 lines to make a rectangle with upper side open
    pygame.draw.line(screen, white, (40, 40), (40, 720), 1)
    pygame.draw.line(screen, white, (40, 720), (560, 720), 1)
    pygame.draw.line(screen, white, (560, 720), (560, 40), 1)
    
    pygame.display.update()

pygame.quit()