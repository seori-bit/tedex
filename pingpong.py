from pygame import *
from random import randint

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
        
racket1 = Player(racket_img, 30, 200, 4, 50, 8)
racket2 = Player(racket_img, 470, 200, 4, 50, 8)
ball = GameSprite(ball_img, 250, 250, 50, 50, 15)

win_width = 500
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
back = (255, 255, 255)
window.fill(back)

finish = False
run = True

speed_x = 3
speed_y = 3


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(win1, (50, 250))

        if ball.rect.x > win_width:
            finish = True
            window.blit(win2, (50, 250))
            run = False

        ball.reset()
        racket2.reset()
        racket1.reset()

    display.update()
    time.delay(50)

#ddddds