import pygame

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Paint")

# Set up the default drawing color and size
color = BLACK
size = 5

# Set up the default tool
tool = "brush"

# Create a surface for drawing
canvas = pygame.Surface((800, 600))

# Set up the font for the tool selector
font = pygame.font.SysFont("Arial", 24)

# Define the function for drawing text
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Define the function for drawing a rectangle
def draw_rect(start_pos, end_pos):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(canvas, color, rect)

# Define the function for drawing a circle
def draw_circle(start_pos, end_pos):
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    pygame.draw.circle(canvas, color, start_pos, radius, size)

# Define the function for erasing
def erase(start_pos, end_pos):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(canvas, WHITE, rect)

# Define the main loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Handle the left mouse button
            if event.button == 1:

                # Handle the tool selection
                if event.pos[0] < 100:
                    if event.pos[1] < 50:
                        tool = "brush"
                    elif event.pos[1] < 100:
                        tool = "rectangle"
                    elif event.pos[1] < 150:
                        tool = "circle"
                    elif event.pos[1] < 200:
                        tool = "eraser"
                    elif event.pos[1] < 250:
                        color = BLACK
                    elif event.pos[1] < 300:
                        color = RED
                    elif event.pos[1] < 350:
                        color = GREEN
                    elif event.pos[1] < 400:
                        color = BLUE
                    elif event.pos[1] < 450:
                        size = 5
                    elif event.pos[1] < 500:
                        size = 10
                    elif event.pos[1] < 550:
                        size = 20

                # Handle the drawing
                else:
                    start_pos = event.pos

            # Handle the right mouse button
            elif event.button == 3:

                # Clear the canvas
                canvas.fill(WHITE)

        elif event.type == pygame.MOUSEBUTTONUP:

            # Handle the drawing
            # Handle the drawing
            if event.button == 1:
                end_pos = event.pos
                if tool == "brush":
                    pygame.draw.line(canvas, color, start_pos, end_pos, size)
                elif tool == "rectangle":
                    draw_rect(start_pos, end_pos)
                elif tool == "circle":
                    draw_circle(start_pos, end_pos)
                elif tool == "eraser":
                    erase(start_pos, end_pos)
                start_pos = end_pos

    # Draw the tool selector
    pygame.draw.rect(screen, WHITE, (0, 0, 100, 600))
    draw_text("Tools:", 10, 10)
    draw_text("Brush", 10, 50)
    draw_text("Rectangle", 10, 100)
    draw_text("Circle", 10, 150)
    draw_text("Eraser", 10, 200)
    draw_text("Colors:", 10, 250)
    pygame.draw.rect(screen, BLACK, (10, 270, 30, 30))
    pygame.draw.rect(screen, RED, (10, 320, 30, 30))
    pygame.draw.rect(screen, GREEN, (10, 370, 30, 30))
    pygame.draw.rect(screen, BLUE, (10, 420, 30, 30))
    draw_text("Sizes:", 10, 470)
    draw_text("5", 10, 510)
    draw_text("10", 10, 560)
    draw_text("20", 10, 610)

    # Draw the canvas
    screen.blit(canvas, (100, 0))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
