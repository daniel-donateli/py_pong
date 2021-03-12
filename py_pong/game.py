import sys
import pygame
from pygame.locals import *

from py_pong.components.window import Window
from py_pong.components.player import Player
from py_pong.components.ball import Ball
from py_pong.components.constants import WHITE

class Game:
  def __init__(self):
    # init pygame modules
    pygame.init()

    # init game components
    self.window = Window()
    self.player_1 = Player(rect_x = 20, rect_y = 200)
    self.player_2 = Player(rect_x = 670, rect_y = 200)
    self.ball = Ball(color = WHITE, width = 10, height = 10)
    self.ball.rect.x = 345
    self.ball.rect.y = 195
    self.clock = pygame.time.Clock()

    # Create sprite group
    self.all_sprites_list = pygame.sprite.Group()
    self.all_sprites_list.add(self.player_1.paddle)
    self.all_sprites_list.add(self.player_2.paddle)
    self.all_sprites_list.add(self.ball)

  def update(self) -> None:
    self.all_sprites_list.update()

    keys = pygame.key.get_pressed()
    # W - player 1 up, S - player 1 down, ARROW_UP - player 2 up, ARROW_DOWN player 2 down
    if keys[K_w]:
      self.player_1.move_up()
    if keys[K_s]:
      self.player_1.move_down()
    if keys[K_UP]:
      self.player_2.move_up()
    if keys[K_DOWN]:
      self.player_2.move_down()
      
    # Check if the ball is bouncing against any of the 4 walls:
    if self.ball.rect.x >= 690:
      self.player_1.score += 1
      self.ball.velocity[0] = -self.ball.velocity[0]
    if self.ball.rect.x <= 0:
      self.player_2.score += 1
      self.ball.velocity[0] = -self.ball.velocity[0]
    if self.ball.rect.y > 490:
      self.ball.velocity[1] = -self.ball.velocity[1]
    if self.ball.rect.y < 0:
      self.ball.velocity[1] = -self.ball.velocity[1]
      
    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(self.ball, self.player_1.paddle) or pygame.sprite.collide_mask(self.ball, self.player_2.paddle):
      self.ball.bounce()

    # Draw sprites on surface
    self.window.draw([self.all_sprites_list], (self.player_1.score, self.player_2.score))

    self.window.update()
    
    self.clock.tick(60)

  def run(self) -> None:
    running = True

    # Game Loop
    while running:
      # Close the window or press Esc to quit
      for event in pygame.event.get():
        if event.type == QUIT:
          running = False
        elif event.type==KEYDOWN:
          if event.key==K_ESCAPE: 
            running = False
      
      self.update()
    
    pygame.quit()
    sys.exit()
