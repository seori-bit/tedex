from pygame import *
from random import *

font.init()
font1 = font.Font(None, 80)
win1 = font1.render('PLAYER 1 WIN!', True, (255, 255, 255))
win2 = font1.render('PLAYER 2 WIN!', True, (180, 0, 0))

racket_img = 'racket.png'
ball_img = 'tenis_ball.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


def bounce_paddle(paddle):
    global SPEED_Y, SPEED_X
    rel_intersect_y = (ball.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
    SPEED_Y = rel_intersect_y * abs(SPEED_X)
    SPEED_X = - SPEED_X * ACCELERATION

    SPEED_Y = max(-MAX_SPEED, min(MAX_SPEED,SPEED_Y))
    SPEED_X = max(-MAX_SPEED, min(MAX_SPEED,SPEED_X))        
racket1 = Player(racket_img, 30, 200, 4, 50, 8)
racket2 = Player(racket_img, 470, 200, 4, 50, 8)
ball = GameSprite(ball_img, 250, 250, 50, 50, 15)


def ball_reset(direction):
    global SPEED_Y, SPEED_X
    ball.rect.center = (win_height // 2, win_width // 2)
    SPEED_X = direction * INIT_SPEED
    SPEED_Y = uniform(-2, 2)




win_width = 500
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
back = (255, 255, 255)
window.fill(back)

finish = False
run = True


WIN_SCORE = 2
score1, score2 = 0, 0
INIT_SPEED = 4
MAX_SPEED = 8
ACCELERATION = 1.05

SPEED_X = INIT_SPEED * choice((-1,1))
SPEED_Y = uniform(-2, 2)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += SPEED_X
        ball.rect.y += SPEED_Y


        if sprite.collide_rect(racket1, ball):
            bounce_paddle(racket1)


        if sprite.collide_rect(racket2, ball):
            bounce_paddle(racket2)

        if ball.rect.y > 450 or ball.rect.y < 0:
            score += 1
            if score2 >= WIN_SCORE:
                finish = True
            else:
                ball_reset(1)

        if ball.rect.x < 0:
            finish = True
            window.blit(win1, (50, 250))

        if ball.rect.x > win_width:
            score += 1
            if score >= WIN_SCORE:
                finish = True
                window.blit(win1, (250,250))
            else:
                ball_reset(-1)

        ball.reset()
        racket2.reset()
        racket1.reset()

    display.update()
    time.delay(50)

#ddddds