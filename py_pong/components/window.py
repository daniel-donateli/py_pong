import pygame
from typing import Tuple, List
from py_pong.components.constants import *

class Window:
  def __init__(self):
    # Create surface
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong!")
  
  def draw(self, sprite_groups: List[pygame.sprite.Sprite], scores: Tuple[int, int]) -> None:
    # Draw black background
    self.screen.fill(BLACK)
    # Draw net
    pygame.draw.line(self.screen, WHITE, [349, 0], [349, 500], 5)
    # Draw sprites
    for sprite in sprite_groups:
      sprite.draw(self.screen)
    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scores[0]), 1, WHITE)
    self.screen.blit(text, (250,10))
    text = font.render(str(scores[1]), 1, WHITE)
    self.screen.blit(text, (420,10))
  
  def update(self) -> None:
    pygame.display.flip()