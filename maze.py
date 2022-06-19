import pgzrun

WIDTH   = 700
HEIGHT  = 490

floor  =  Actor('floor',topleft=(0,0))
player =  Actor('player',topleft=(70,0))

def draw():
    screen.clear()
    for y in range(7):
        for x in range(10):
            floor.topleft=(70*x,70*y)
            floor.draw()
    player.draw()

pgzrun.go()


