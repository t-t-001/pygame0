import pgzrun
import random

WIDTH   =  800
HEIGHT  =  600

shooter_hp = 10
enemy_hp   = 30
s_missiles = []
turn       = False

shooter = Actor('shooter.png',(400,500))
enemy   = Actor('enemy.png',(400,100))

def draw():
    screen.clear()
    for missile in s_missiles:
        missile.draw()
    shooter.draw()
    enemy.draw()
    screen.draw.text('Enemy HP = ' + str(enemy_hp),(50,50),color='YELLOW',fontsize=32)
    screen.draw.text('Shooter HP = ' + str(shooter_hp),(600,50),color='YELLOW',fontsize=32)

def update():
    global enemy_hp,turn
    if keyboard.left:
        if shooter.x > 47:
            shooter.x -= 3
    if keyboard.right:
        if shooter.x < WIDTH -47:
            shooter.x += 3
    if turn :
        enemy.x  +=  5
        if enemy.x > WIDTH:
            turn =  False
    else:
        enemy.x -= 5
        if enemy.x < 0:
            turn = True

    for missile in s_missiles:
        missile.y -= 10
        rect = Rect(missile.topleft,(16,22))
        if enemy.colliderect(rect):
            enemy_hp -= 1
            s_missiles.remove(missile)
        else:
            if missile.y < 0:
                s_missiles.remove(missile)

def on_key_down(key):
    global s_missiles
    if key == keys.SPACE:
        s_missiles.append(Actor('smissile.png',shooter.pos))

pgzrun.go()
