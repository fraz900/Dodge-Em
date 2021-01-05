#Imports
import pygame, sys
from pygame.locals import *
import random, time
import pyautogui
try:
      file = open("scores.txt","r").close()
except:
      file = open("scores.txt","w").close()
      

#Initializing 
pygame.init()
 

FPS = 60
FramePerSec = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
global SCORE
SCORE = 0

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy1.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40)
                                                 , 0))
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            pygame.mixer.Sound('enemy_spawn.wav').play()
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def reset(self):
            self.surf = pygame.Surface((50,80))
            self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40)
                                                 , 0))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player2.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (150, 500))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    def reset(self):
          self.surf = pygame.Surface((50, 100))
          self.rect = self.surf.get_rect(center = (150, 500))
class died(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("died2.png")
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (100, 250))


class retry(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("retry.png")
            self.surf = pygame.Surface((50,100))
            self.rect = self.surf.get_rect(center = (100,500))
      def get_rect(self):
            return(self.rect)
class quit1(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("quit.png")
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (100, 300))
      def get_rect(self):
            return(self.rect)

class title(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("enemy.png")
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (85, 100))
class credit(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("credits.png")
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (85, 550))
      def get_rect(self):
            return(self.rect)


class title_card(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("title_card.png")
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (85, 300))    
P1 = Player()
E1 = Enemy()
 

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
PAGE = pygame.sprite.Group() 
#R = retry()
Q = quit1()
T = title()
T1 = title_card()
C = credit()
#PAGE.add(R)
PAGE.add(Q)
PAGE.add(T)
PAGE.add(C)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
won = False
running = True
while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
        if event.type == pygame.MOUSEBUTTONDOWN:
              x,y = event.pos
              if not running:
                  #if R.get_rect().collidepoint(x,y):
                   #     print("retry")
                    #    SCORE = 0
                     #   running = True
                      #  P1.reset()
                       # E1.reset()
                    if Q.get_rect().collidepoint(x,y):
                        pygame.quit()
                        sys.exit()
                    if C.get_rect().collidepoint(x,y):
                        pygame.mixer.Sound('credit.wav').play()
                        myFont = pygame.font.SysFont("Times New Roman", 30)
                        DISPLAYSURF.fill(BLACK)
                        message = "Thank you for playing!"
                        Message = myFont.render(message,True,WHITE)
                        DISPLAYSURF.blit(Message,(85,100))
                        pygame.display.update()
                        time.sleep(6)
                        DISPLAYSURF.fill(BLACK)
                        pygame.display.update()
                        message = "developed by:"
                        Message = myFont.render(message,True,WHITE)
                        DISPLAYSURF.blit(Message,(85,100))
                        pygame.display.update()
                        time.sleep(3)
                        message1 = "Fraser Clapham"
                        Message1 = myFont.render(message1,True,WHITE)
                        DISPLAYSURF.blit(Message1,(85,300))
                        pygame.display.update()
                        time.sleep(6)
                        DISPLAYSURF.fill(BLACK)
                        pygame.display.update()
                        message = "created for:"
                        Message = myFont.render(message,True,WHITE)
                        DISPLAYSURF.blit(Message,(85,100))
                        pygame.display.update()
                        time.sleep(3)
                        message1 = "2484 October challenges"
                        Message1 = myFont.render(message1,True,WHITE)
                        DISPLAYSURF.blit(Message1,(85,300))
                        pygame.display.update()
                        time.sleep(6)
                        DISPLAYSURF.fill(BLACK)
                        pygame.display.update()
                        message = "coded in:"
                        Message = myFont.render(message,True,WHITE)
                        DISPLAYSURF.blit(Message,(85,100))
                        pygame.display.update()
                        time.sleep(3)
                        message1 = "48 hours"
                        Message1 = myFont.render(message1,True,WHITE)
                        DISPLAYSURF.blit(Message1,(85,300))
                        pygame.display.update()
                        time.sleep(6)
                        DISPLAYSURF.fill(BLACK)
                        pygame.display.update()
                        message = "Hope you had fun!"
                        Message = myFont.render(message,True,WHITE)
                        DISPLAYSURF.blit(Message,(85,300))
                        pygame.display.update()
                        time.sleep(6)
                        DISPLAYSURF.fill(BLACK)
                        
                        DISPLAYSURF.blit(T.image,T.rect)
                        DISPLAYSURF.blit(T1.image,T1.rect)
                        pygame.display.update()
                        time.sleep(10)
                        pygame.quit()
                        sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.fill(WHITE)
 
    if running:
          for entity in all_sprites:
              DISPLAYSURF.blit(entity.image, entity.rect)
              entity.move()
    elif not running:
          black=(0,0,0)
          myFont = pygame.font.SysFont("Times New Roman", 60)
          message = "Your score is "+(str(SCORE))
          message1 = "Highscore = "+ str(top)
          Message = myFont.render(message,True,black)
          Message1 = myFont.render(message1,True,black)
          for entity in PAGE:
                DISPLAYSURF.blit(entity.image, entity.rect)
          DISPLAYSURF.blit(Message,(10,450))
          DISPLAYSURF.blit(Message1,(10,350))
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('loss.wav').play()
          DISPLAYSURF.fill(RED)
          D = died()
          DISPLAYSURF.blit(D.image,D.rect)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          entry = (str(SCORE)+"\n")
          file = open("scores.txt","a")
          file.write(entry)
          file.close()
          file = open("scores.txt","r")
          scores = file.read()
          file.close()
          scores = scores.split("\n")
          top = 0
          for s in scores:
                if not s == "":
                      s = int(s)
                      if s > top:
                            top = s

          time.sleep(5)
          if SCORE > 10:
                pyautogui.alert("You won, well done")
                won = True
          DISPLAYSURF.fill(WHITE)
          running = False
          #pygame.quit()
          #sys.exit()
          
    pygame.display.update()
    FramePerSec.tick(FPS)
