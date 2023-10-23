import pygame
import math
import random

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
white_radius = 15
red_radius = 22
yellow_radius = 32
green_radius = 40

radius_order = [white_radius, red_radius, yellow_radius, green_radius]

box_bottom = 720 - white_radius 
box_left = 40 + white_radius
box_right = 560 - white_radius

balls = []
balls_to_add = []
balls_to_remove = []

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
            horizontal_speed = 0 
            balls.append([ball_x, ball_y, ball_speed, horizontal_speed, white, white_radius])
            
    
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            dx = balls[i][0] - balls[j][0]
            dy = balls[i][1] - balls[j][1]

            distance = math.sqrt(dx **2 + dy **2)
            if distance < balls[i][5] + balls[j][5]:
                # check if the balls are of same color
                if balls[i][4] == balls[j][4]:
                    color_index = color_order.index(balls[i][4])
                    if color_index + 1 < len(color_order):
                        # add a new ball with next color
                        # sum horizontal speed after collision
                        new_x = (balls[i][0] + balls[j][0]) / 2 + random.uniform(-1,1)
                        new_y = (balls[i][1] + balls[j][1]) / 2 + random.uniform(0,1)
                        balls_to_add.append([new_x, new_y, balls[i][2] , balls[i][3] + balls[j][3],  color_order[color_index + 1], radius_order[color_index + 1]])
                        # remove the balls of same color
                    balls_to_remove.append(balls[i])
                    balls_to_remove.append(balls[j])
                    # update index after remove
                    i -= 1
                    break
                # if they touch but not of same color
                else:
                    # check overlap
                    overlap = balls[i][5] + balls[j][5] - distance
                    dx = dx / distance
                    dy = dy / distance
                    balls[i][0] += dx * overlap / 2
                    balls[i][1] += dy * overlap / 2
                    balls[j][0] -= dx * overlap / 2
                    balls[j][1] -= dy * overlap / 2
                    
                    # update speed of both balls when they collide
                    balls[i][2] = 0 
                    balls[j][2] = 0
                    balls[i][3] *= -0.5
                    balls[j][3] *= -0.5

    # remove and add balls
    for ball in balls_to_remove:
        if ball in balls:
            balls.remove(ball)
    for ball in balls_to_add:
        balls.append(ball)
    # empty the lists
    balls_to_remove.clear()
    balls_to_add.clear()
    # draw balls
    for ball in balls:
        box_bottom = 720 - ball[5]
        box_left = 40 + ball[5]
        box_right = 560 - ball[5]
        if ball[1] >= box_bottom:
            ball[1] = box_bottom
        elif ball[1] < box_bottom:
            ball[1] += ball[2]
        # else:
        #     ball[1] = box_bottom
        #     ball[2] *= -0.5
        
        # update x position of ball
        ball[0] += ball[3]
        # check if ball is out of box horizontally
        if ball[0] < box_left:
            ball[0] = box_left + 1
            ball[3] *= -0.5
        elif ball[0] > box_right:
            ball[0] = box_right - 1
            ball[3] *= -0.5
        any_ball = pygame.draw.circle(screen, ball[4], (ball[0], ball[1]), ball[5])
    # draw 3 lines to make a rectangle with upper side open
    pygame.draw.line(screen, white, (40, 40), (40, 720), 1)
    pygame.draw.line(screen, white, (40, 720), (560, 720), 1)
    pygame.draw.line(screen, white, (560, 720), (560, 40), 1)
    
    pygame.display.update()

pygame.quit()