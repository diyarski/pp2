import pygame, math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    mouse_down = False
    shape_mode = None

    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    shape_mode = 'circle'
                elif event.key == pygame.K_q:
                    shape_mode = 'rect'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_l:
                    shape_mode = None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
                elif event.button == 2:
                    if mode != 'eraser':
                        mode = 'eraser'
                    else:
                        mode = 'blue'
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                if mouse_down:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            if shape_mode == 'circle':
                drawCicleBetween(screen, i, points[i], points[i + 1], radius)
            elif shape_mode == 'rect':
                drawRectBetween(screen, i, points[i], points[i + 1], radius)
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
def drawCicleBetween(screen, index, start, end, width):
    color = (255, 255, 255)
    radius = int(math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2))
    pygame.draw.circle(screen, color, start,radius, width)
    
def drawRectBetween(screen, index, start, end, width):
    color = (255, 255, 255)
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, width)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
   
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
        
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
        
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
