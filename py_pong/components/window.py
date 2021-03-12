from pygame.draw import line
import pygame.display as display
from py_pong.components.constants import *

class Window:
  def __init__(self):
    self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.set_caption("Pong!")
  
  def draw(self, sprite_groups):
    self.screen.fill(BLACK)
    line(self.screen, WHITE, [349, 0], [349, 500], 5)
    for sprite in sprite_groups:
      sprite.draw(self.screen)
  
  def update(self):
    display.flip()