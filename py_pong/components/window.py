from pygame.draw import line
import pygame.display as display
from py_pong.components.colors import *

class Window:
  def __init__(self, width: int = 800, height: int = 600):
    self.screen = display.set_mode((width, height))
    display.set_caption("Pong!")
  
  def draw(self, sprite_groups):
    self.screen.fill(BLACK)
    line(self.screen, WHITE, [349, 0], [349, 500], 5)
    for sprite in sprite_groups:
      sprite.draw(self.screen)
  
  def update(self):
    display.flip()