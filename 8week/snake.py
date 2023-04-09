import pygame, time, random

snake_speed = 15
snake_level = 1

window_x = 720
window_y = 480

# define colors

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
fruit_timer = pygame.time.get_ticks()

direction = 'RIGHT'
change_to = direction

score = 0

def show_score_and_level(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + ' Level: ' + str(snake_level), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
    
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()
    
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()
    quit()

# main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    # if two keys are pressed at the same time we don't want for the snake tpo divide in two directions at the same time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # movement of the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] +=10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    # main mechaniks of the game
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += (random.randrange(1, 4)*10)
        fruit_spawn = False
    else:
        snake_body.pop()
    # loop for the increase of level and speed of the snake
    if score >= snake_level*30:
        snake_level +=1
        snake_speed +=3
    current_time = pygame.time.get_ticks()
    if current_time - fruit_timer > 5000:
        fruit_spawn = False
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True
        fruit_timer = pygame.time.get_ticks()
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    # displaying score countinuously
    show_score_and_level(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame per second/Refresh Rate
    fps.tick(snake_speed)
