import pygame


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
white_radius = 5
red_radius = 7
yellow_radius = 13
green_radius = 20

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
            balls.append([ball_x, ball_y])
            
    for ball in balls:
        # bacasue downward in pygame is positive
        if ball[1] < 720 - white_radius:
            ball[1] += ball_speed
        else:
            ball[1] = 720 - white_radius
        white_ball = pygame.draw.circle(screen, white, (ball[0], ball[1]), white_radius)
    # draw 3 lines to make a rectangle with upper side open
    pygame.draw.line(screen, white, (40, 40), (40, 720), 1)
    pygame.draw.line(screen, white, (40, 720), (560, 720), 1)
    pygame.draw.line(screen, white, (560, 720), (560, 40), 1)
    
    pygame.display.update()

pygame.quit()