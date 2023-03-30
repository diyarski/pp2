# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored

import pygame

pygame.init()

# Set the window size
WINDOW_SIZE = (500, 500)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Moving Ball")

# Set up the ball
ball_position = [WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2]
ball_radius = 25
ball_colour = (255, 0, 0)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_position[1] -=20
            elif event.key == pygame.K_DOWN:
                ball_position[1] +=20
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += 20
            elif event.key == pygame.K_LEFT:
                ball_position[0] -=20
    # ensure ball stays on the screen
    ball_position[0] = max(ball_radius, min(WINDOW_SIZE[0] - ball_radius, ball_position[0]))
    ball_position[1] = max(ball_radius, min(WINDOW_SIZE[1] - ball_radius, ball_position[1]))

    # clear the screen
    window.fill((255, 255, 255))

    # draw the ball
    pygame.draw.circle(window, ball_colour, ball_position, ball_radius)

    # update the screen
    pygame.display.flip()
