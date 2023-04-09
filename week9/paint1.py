import pygame
import random

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)
radius = 5
color = (0, 0, 0)

# Function to draw a rectangle
def draw_rect(surface, color, rect):
    pygame.draw.rect(surface, color, rect)

# Function to draw a circle
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Function to erase with a white circle
def erase(surface, pos, radius):
    pygame.draw.circle(surface, (255, 255, 255), pos, radius)

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

try:
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration

        # Adding color selection functionality
        if e.type == pygame.KEYDOWN:
            if e.unicode == 'r':
                color = (255, 0, 0) # Red
            elif e.unicode == 'g':
                color = (0, 255, 0) # Green
            elif e.unicode == 'b':
                color = (0, 0, 255) # Blue
            elif e.unicode == 'w':
                color = (255, 255, 255) # White
            elif e.unicode == 'k':
                color = (0, 0, 0) # Black

        # Adding rectangle drawing functionality
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                draw_on = True
                start_pos = e.pos
            elif e.button == 3:
                draw_on = True
                start_pos = e.pos
                rect_pos = e.pos

        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                draw_on = False
                end_pos = e.pos
                draw_rect(screen, color, pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])))
            elif e.button == 3:
                draw_on = False
                end_pos = e.pos
                radius = int(((end_pos[0]-rect_pos[0])**2 + (end_pos[1]-rect_pos[1])**2)**0.5)
                draw_circle(screen, color, rect_pos, radius)

        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                if e.buttons == (1, 0, 0):
                    pygame.draw.circle(screen, color, e.pos, radius)
                    erase(screen, e.pos, radius)
                    roundline(screen, color, e.pos, last_pos, radius)
                elif e.buttons == (0, 0, 1):
                    pygame.draw.circle(screen, (255, 255, 255), e.pos, radius)
                elif e.buttons == (0, 1, 0):
                    pygame.draw.line(screen, color, e.pos, last_pos, radius*2)
                elif e.buttons == (0, 0, 0):
                    pass

            last_pos = e.pos

        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()
