import pygame
from pygame import *

pygame.init()

width = 700
height = 500
clock = time.Clock()
FPS = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame window')

background = (135, 206, 235)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:  
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - self.rect.height - 5:  
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:  
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < height - self.rect.height - 5: 
            self.rect.y += self.speed



racket1 = Player('raketla.png', 30, 200, 20, 100, 4) 
racket2 = Player('raketla.png', 520, 200, 20, 100, 4) 
ball = GameSprite('tennis_ball.png', 200, 200, 50, 50, 4)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            

    screen.fill(background)  
    racket1.update_r()
    racket2.update_l()
    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)