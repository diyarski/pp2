import pygame, math

pygame.init()
sc = pygame.display.set_mode((800, 450))
sc.fill((255, 255, 255))
pygame.display.flip()

color = (0, 0, 0)
radius = 10
Draw = False
spos = None
tool = 3

f1 = pygame.font.SysFont(None, 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                radius -= 2
            elif event.key == pygame.K_p:
                radius += 2
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_q:
                color = (0, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_c:
                tool = 1
            elif event.key == pygame.K_s:
                tool = 2
            elif event.key == pygame.K_f:
                tool = 3
            elif event.key == pygame.K_e:
                tool = 4
            elif event.key == pygame.K_1:
                tool = 5
            elif event.key == pygame.K_2:
                tool = 6
            elif event.key == pygame.K_3:
                tool = 7
            elif event.key == pygame.K_4:
                tool = 8
            elif event.key == pygame.K_a:
                sc.fill((255, 255, 255))
                pygame.display.update()

        if tool == 2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]

                    pygame.draw.rect(sc, color, (spos[0], spos[1], w, h))
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False
        if tool == 5:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos
                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]
                    

                    pygame.draw.rect(sc, color, (spos[0], spos[1], min(w, h), min(w, h)))
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False
        if tool == 6:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos

                    w1, h1 = spos
                    w2, h2 = pos
                    w3, h3 = w2, h1

                    pygame.draw.polygon(sc, color, [(w1, h1), (w2, h2), (w3, h3)], 0)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False
        if tool == 7:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos
                    w1, h1 = spos
                    w2, h2 = pos
                    h = abs(h2 - h1)
                    w = h * 2 / math.sqrt(3)
                    w3, h3 = (w1+w2)/2, h1+h
                    pygame.draw.polygon(sc, color, [(w1,h1), (w2,h2), (w3,h3)], 0)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False
        if tool == 8:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos
                    w1, h1 = spos
                    w2, h2 = pos
                    w3, h3 = (w1+w2) // 2, (h1+h2) // 2
                    w, h = abs(w2-w1), abs(h2-h1)
                    pygame.draw.polygon(sc, color,[(w3,h1), (w2,h3), (w3,h2), (w1,h3)], 0)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False
        if tool == 1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Draw = True
                spos = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if Draw:
                    pos = event.pos

                    w = pos[0] - spos[0]
                    h = pos[1] - spos[1]

                    pygame.draw.circle(sc, color, (spos[0], spos[1]), w//2)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Draw = False

        if tool == 3:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, color, mPos, radius)
                pygame.display.flip()

        if tool == 4:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                mPos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, (255, 255, 255), mPos, radius)
                pygame.display.flip()


        pygame.display.update()
