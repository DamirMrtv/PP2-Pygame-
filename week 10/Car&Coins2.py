import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = [1,2,3,4,5]
SCORE = 0
SPED = 5

font = pygame.font.SysFont("Times new roman", 60)
font_small = pygame.font.SysFont("Times new roman", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("./Street.png")

 
Screen = pygame.display.set_mode((400,600))
Screen.fill(WHITE)
pygame.display.set_caption("Oncomming traffic")

music = pygame.mixer.Sound("./background.wav")
music.play(loops = -1)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
                                                 

      def move(self):
        self.rect.move_ip(0,SPED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Money(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.image = pygame.image.load("./coin.png")
         self.surf = pygame.Surface((32,30))
         self.rect = self.surf.get_rect(center = (random.randint(30,SCREEN_WIDTH-30), 0))

     def move(self):
         global SCORE
         self.rect.move_ip(0,SPED)
         if (self.rect.bottom > 600):
             self.rect.top = 0
             self.rect.center = (random.randint(40,SCREEN_WIDTH-30),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

P1 = Player()
E1 = Enemy()
C1 = Money()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
      
    SPED = random.choice(SPEED)
    #SPED = random.randint(1,5)
    for event in pygame.event.get():      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    Screen.blit(background, (0,0))
    sc = font_small.render("Coins:" + str(SCORE), True , BLACK)
    Screen.blit(sc, (325,10))

    for entity in all_sprites:
        Screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('./eat.ogg').play()
        SCORE += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40,SCREEN_WIDTH-30),0)
    if pygame.sprite.spritecollideany(P1, enemies):
          music.stop()
          pygame.mixer.Sound('./crash.wav').play()
          time.sleep(1)
                   
          Screen.fill(RED)
          Screen.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
    