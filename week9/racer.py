import pygame, random, sys, os, time
from pygame.locals import *

windowwidth = 800
windowheight = 600
textcolor = (255, 255, 255)
backgroundcolor = (0, 0, 0)
fps = 40
baddieminsize = 10
baddiemaxsize = 10
baddieminspeed = 4
baddiemaxspeed = 6
addnewbaddierate = 3
playermoverate = 5
count = 3
coinspeed = 5
coinsize = 8
addnewcoinrate = 200

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
    
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHasHitCoins(playerRect, coins):
    for c in coins:
        if playerRect.colliderect(c['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textcolor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 30)
# sounds
gameOverSound = pygame.mixer.Sound(r'sounds\car_crash.wav')
pygame.mixer.music.load(r'music\No_Role_Modelz.mp3')
laugh = pygame.mixer.Sound(r'sounds\casual_laugh.wav')
# images
playerImage = pygame.image.load(r'pngFiles\car.png')
car3 = pygame.image.load(r'pngFiles\car2.png')
car4 = pygame.image.load(r'pngFiles\car3.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load(r'pngFiles\car1.png')
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load(r'pngFiles\left_wall.png')
wallRight = pygame.image.load(r'pngFiles\right_wall.png')
coinImage = pygame.image.load(r'pngFiles\Coin.png')

#"Start" screen
drawText('Press space to start the game.', font, windowSurface, (windowwidth / 3) - 30, (windowheight / 3))
drawText('          And Enjoy', font, windowSurface, (windowwidth / 3), (windowheight / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
pygame.display.update()
zero = 0
if not os.path.exists("data/save.dat"):
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()
while(count > 0):
    # start the game
    baddies = []
    coins = []
    coinscore = 0
    score = 0
    playerRect.topleft = (windowwidth / 2, windowheight - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    coinsAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    lastBaddieTime = time.time()
    lastCoinTime = time.time()

    while True:
        score +=1
        baddiespeed = random.randrange(baddieminspeed, baddiemaxspeed)
        if coinscore >= 10:
            baddiespeed +=5
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('z'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()
                
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False
                
        if not reverseCheat and not slowCheat:
            if (time.time()-lastBaddieTime)* 20 >= 1:
                baddieAddCounter += 1
                lastBaddieTime = time.time()
        if not reverseCheat and not slowCheat:
            if (time.time() - lastCoinTime) >= 1:
                coinsAddCounter +=1
        if baddieAddCounter == addnewbaddierate:
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect': pygame.Rect(random.randint(20, 780), 0 - baddieSize, 23, 47),
                         'speed': baddiespeed,
                         'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect' : pygame.Rect(0, 0, 20, 800),
                        'speed': baddiespeed,
                        'surface': pygame.transform.scale(wallLeft, (23, 47))
                        }
            baddies.append(sideLeft)
            sideRight = {'rect': pygame.Rect(780, 0, 780, 800),
                         'speed': baddiespeed,
                         'surface': pygame.transform.scale(wallRight, (780, 800)),
                         }
            baddies.append(sideRight)
        if coinsAddCounter == addnewcoinrate:
            coinsAddCounter = 0
            newCoin = {'rect': pygame.Rect(random.randint(20, 780), 0 - coinsize, 20, 20),
                       'speed': random.randint(coinspeed, coinspeed),
                       'surface': pygame.transform.scale(coinImage, (40, 40)),
                       }
            coins.append(newCoin)

        # move the player around
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * playermoverate, 0)
        if moveRight and playerRect.right < windowwidth:
            playerRect.move_ip(playermoverate, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * playermoverate)
        if moveDown and playerRect.bottom < windowheight:
            playerRect.move_ip(0, playermoverate)
        
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)
        for b in baddies[:]:
            if b['rect'].top > windowheight:
                baddies.remove(b)

        for c in coins:
            c['rect'].move_ip(0, c['speed'])
        for c in coins[:]:
            if c['rect'].top > windowheight:
                coins.remove(c)
        
        # Draw the game world on the window
        windowSurface.fill(backgroundcolor)

        # Draw the score and top score
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)
        drawText('Coins: %s' % (coinscore), font, windowSurface, 700, 0)

        windowSurface.blit(playerImage, playerRect)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
        for c in coins:
            windowSurface.blit(c['surface'], c['rect'])
        pygame.display.update()

        # Check if any of the car have hit the player
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break
        mainClock.tick(fps)
        if playerHasHitCoins(playerRect, coins):
            coins.remove(c)
            coinscore += random.randrange(1, 3)

    # "Game Over" screen
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)
    if (count == 0):
        laugh.play()
        drawText('Game over', font, windowSurface, (windowwidth / 3), (windowheight / 3))
        drawText('Press space to play again.', font, windowSurface, (windowwidth / 3) - 80, (windowheight / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()
