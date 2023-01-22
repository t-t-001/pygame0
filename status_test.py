import pgzrun
import random

WIDTH = 400
HEIGHT = 600

rocket = Actor('rocket' , center=(200,300))

star  = []
for i in range(20):
    rect = Rect((random.randrange(WIDTH),
                 random.randrange(HEIGHT)),(2,2))
    star.append(rect)

speed        =  0      # 速度
acceleration =  0.1    # 加速度
key_flg      =  False  # UPキーが押されるとTrue
status       =  0      # 0:Opening、1:ゲーム中

def draw():
    global  status
    screen.clear()
    #星の描画
    for i in range(20):
        screen.draw.rect(star[i],'WHITE')
    #着陸台の描画
    for i in range(50):
        screen.draw.line((150-i*3,550+i),(250+i*3,550+i),'GRAY')
    if status == 0: #オープニング
        #ロケットの炎
        for i in range(10):
            screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
        #ゲームタイトル
        screen.draw.text("Moon Lander",(50,100),owidth=1.5,ocolor='YELLOW',color='BLACK',fontsize=64)
    elif status == 1: #ゲーム中
        if key_flg: #UPキー押されたら炎噴射
            for i in range(10):
                screen.draw.circle(rocket.midbottom,i+1,(255,i*20,0))
    rocket.draw()

def on_key_down(key):
    global status
    if key ==  keys.SPACE:
        if status  ==  0:
            status = 1
def update():
    global speed
    global acceleration
    global key_flg
    global status
    if status == 1:
        if keyboard.up:
            key_flg = True
            acceleration = -0.1
        else:
            key_flg  =  False
            acceleration = 0.1
        speed += acceleration
        rocket.y += speed

pgzrun.go()
