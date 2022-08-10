import pygame as pg
import sys
import time
import random

pg.init()
width = 600
height = 600
displayWindow = pg.display.set_mode((width, height))
paddle = pg.rect.Rect((width/2-40, height-20, 80, 20))
ball = pg.Vector2((paddle.x+40, height-30))
ballSpeed = pg.Vector2((10, 10))

clock = pg.time.Clock()

speed = 10
target_fps = 60
dt = 0
lastTime = time.time()

scoreFont=pg.font.Font("BalooBhai2-Bold.ttf",26)
scoreLabel=scoreFont.render("Score:0",(0,0,0),(135, 206, 235))
scoreRect=scoreLabel.get_rect()
scoreRect.center=(60,20)

gameOverFont=pg.font.Font("BalooBhai2-Bold.ttf",70)
gameOverLabel=gameOverFont.render("Game Over!",(0,0,0),(0,0,0))
gameOverRect=gameOverLabel.get_rect()
gameOverRect.center=(300,300)


gameStarted = False
gamescore = 0
gameLost = False

def gameOver():
    displayWindow.blit(gameOverLabel,gameOverRect)
    pg.display.update()
    pg.time.delay(3000)

def checkCollision(ball):
    global gamescore, gameLost,scoreLabel,scoreRect
    if ball.y <= 0:
        ballSpeed.y = -ballSpeed.y
    if ball.x <= 0 or ball.x >= width:
        ballSpeed.x = -ballSpeed.x
    if (ball.x > paddle.x and ball.x < paddle.x+80) and (ball.y > paddle.y-10):
        ballSpeed.y = -ballSpeed.y
        gamescore += 1
        scoreLabel=scoreFont.render(f"Score:{gamescore}",(0,0,0),(135, 206, 235))
        # displayWindow.blit(scoreLabel,scoreRect)
    if ball.y+10 >= height:
        gameLost = True
        gameOver()

while True:
    if gameLost == True:
        pg.quit()
        print("Exited Successfully")
      

    newTime = time.time()
    dt = newTime-lastTime
    lastTime = newTime

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and gameStarted == False:
                gameStarted = True
                ballSpeed.y = -ballSpeed.y
                flag = random.randint(0, 1)
                ballSpeed.x = random.randint(5, 10)
                if flag == 0:
                    ballSpeed.x = -ballSpeed.x

    keys = pg.key.get_pressed()
    # if keys[pg.K_DOWN]:
    #     paddle.y+=speed*dt*target_fps
    # if keys[pg.K_UP]:
    #     paddle.y-=speed*dt*target_fps
    if keys[pg.K_RIGHT]:
        if paddle.x+80 < width:
            paddle.x += speed*dt*target_fps

    if keys[pg.K_LEFT]:
        if paddle.x > 0:
            paddle.x -= speed*dt*target_fps

    if gameStarted == False:
        ball.x = paddle.x+40

    else:
        ball.y += ballSpeed.y*dt*target_fps
        ball.x += ballSpeed.x*dt*target_fps

    checkCollision(ball)
    displayWindow.fill((255, 255, 255))
    displayWindow.blit(scoreLabel,scoreRect)
    pg.draw.rect(displayWindow, (135, 206, 235), paddle)
    pg.draw.circle(displayWindow, (0, 0, 0), ball, 10)
    pg.display.update()
    # clock.tick(20)
