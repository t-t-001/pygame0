import pgzrun

WIDTH   = 700
HEIGHT  = 490

# MAP情報(1の場所がbox)
map_data = [[1,0,1,0,0,0,0,1,0,0],
            [1,0,1,1,1,0,1,1,1,0],
            [1,0,0,0,0,0,0,0,0,0],
            [1,1,0,1,1,1,1,1,1,0],
            [0,0,0,1,0,0,0,1,1,0],
            [0,1,1,1,0,1,0,0,0,1],
            [0,0,0,0,0,1,0,1,0,0]]
# Playerの現在位置
location  =  [0,1]
#Player
player =  Actor('player',topleft=(70,0))
#床のタイル
floor  =  Actor('floor' ,topleft=(0,0))
#箱
box    =  Actor('box'   ,topleft=(0,0))
#出口の看板
exit   =  Actor('exit'  ,topleft=(630,420))

def draw():
    screen.clear()
    for y in range(7):
        for x in range(10):
            floor.topleft=(70*x,70*y)
            floor.draw()
            if map_data[y][x] == 1:
                box.topleft = (70*x,70*y)
                box.draw()
    exit.draw()
    player.draw()

def on_key_down(key):
    if key == keys.UP:
        if location[0] >= 1:
            if map_data[location[0]-1][location[1]] != 1:
                location[0] -= 1
                player.y  -=  70
    if key == keys.DOWN:
        if location[0] <= 5:
            if map_data[location[0]+1][location[1]] != 1:
                location[0]  +=  1
                player.y     +=  70
    if key == keys.LEFT:
        if location[1] >= 1:
            if map_data[location[0]][location[1]-1] != 1:
                location[1] -= 1
                player.x    -= 70
    if key == keys.RIGHT:
        if location[1] <= 8:
            if map_data[location[0]][location[1]+1] != 1:
                location[1] += 1
                player.x   +=  70 

pgzrun.go()


