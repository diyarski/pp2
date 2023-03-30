'''
Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
For moving Mickey's hands you can use: pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144
'''

import pygame
import time
import math
import sys

pygame.init()

# Set up the window
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey's Clock")

# Load the image of the clock face
clock_face = pygame.image.load('jpgFiles\mickey_clock.jpg').convert_alpha()
clock_face = pygame.transform.smoothscale(clock_face, (800, 800))
# Load the images of Mickey Mouse's hands
minute_hand = pygame.image.load('pngFiles\mickey_right_hand.png').convert_alpha()
minute_hand = pygame.transform.smoothscale(minute_hand, (400, 300))


second_hand = pygame.image.load('pngFiles\mickey_left_hand.png').convert_alpha()
second_hand = pygame.transform.smoothscale(second_hand, (400, 400))


# Set the initial angle of the hands to match the current time
current_time = time.localtime()
minute_angle = math.pi/2 - (current_time.tm_min/60) * 2 * math.pi
second_angle = math.pi/2 - (current_time.tm_sec/60) * 2 * math.pi

# Run the clock loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the clock face
    win.blit(clock_face, (0, 0))

    # Draw the minute hand
    minute_hand_rotated = pygame.transform.rotate(minute_hand, math.degrees(minute_angle))
    win.blit(minute_hand_rotated, (400-minute_hand_rotated.get_width()/2, 400-minute_hand_rotated.get_height()/2))

    # Draw the second hand
    second_hand_rotated = pygame.transform.rotate(second_hand, math.degrees(second_angle))
    win.blit(second_hand_rotated, (400-second_hand_rotated.get_width()/2, 400-second_hand_rotated.get_height()/2))

    # Update the angles of the hands
    current_time = time.localtime()
    minute_angle = math.pi/2 - (current_time.tm_min/60) * 2 * math.pi
    second_angle = math.pi/2 - (current_time.tm_sec/60) * 2 * math.pi

    # Update the display
    pygame.display.update()
