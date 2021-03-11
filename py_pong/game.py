import sys
import pygame
from pygame.locals import *

from py_pong.components.window import Window
from py_pong.components.player import Player
from py_pong.components.ball import Ball

class Game:
  def __init__(self):
    pygame.init()
    self.window = Window(750, 500)
    self.player_1 = Player(20, 200)
    self.player_2 = Player(670, 200)
    self.ball = Ball()
    self.clock = pygame.time.Clock()
    self.all_sprites_list = pygame.sprite.Group()
    self.all_sprites_list.add(self.player_1.paddle)
    self.all_sprites_list.add(self.player_2.paddle)

  def update(self):
    self.all_sprites_list.update()

    self.window.draw([self.all_sprites_list])
    self.window.update()
    
    self.clock.tick(60)

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == QUIT:
          running = False
        elif event.type==KEYDOWN:
          if event.key==K_ESCAPE: 
            running = False
      self.update()
    
    pygame.quit()
    sys.exit()
