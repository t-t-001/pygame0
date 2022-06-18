import pgzrun
WIDTH  = 400
HEIGHT = 200

alien = Actor('alien',center=(200,100))
plusminusx = 1
plusminusy = 1
def draw():
    screen.clear()
    alien.draw()
def update():
    global plusminusx
    global plusminusy
    alien.x += plusminusx
    alien.y += plusminusy
    if alien.x == 400:
        plusminusx = -1
    elif alien.x == 0:
        plusminusx = 1
    if alien.y == 200:
        plusminusy = -1
    elif alien.y == 0:
        plusminusy = 1





pgzrun.go()
