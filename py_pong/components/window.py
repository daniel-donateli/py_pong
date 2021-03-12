from pygame.draw import line
import pygame.display as display
from py_pong.components.constants import *

class Window:
  def __init__(self):
    # Create surface
    self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.set_caption("Pong!")
  
  def draw(self, sprite_groups) -> None:
    # Draw black background
    self.screen.fill(BLACK)
    # Draw net
    line(self.screen, WHITE, [349, 0], [349, 500], 5)
    # Draw sprites
    for sprite in sprite_groups:
      sprite.draw(self.screen)
  
  def update(self) -> None:
    # Blit
    display.flip()