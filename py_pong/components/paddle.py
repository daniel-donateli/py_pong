import pygame
from typing import Tuple
from py_pong.components.constants import BLACK

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color: Tuple[int, int, int], width: int, height: int):
    # Call Sprite constructor
    super().__init__()
        
    # Pass in the color of the paddle, and its x and y position, width and height.
    # Set the background color and set it to be transparent
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
 
    # Draw the paddle
    pygame.draw.rect(self.image, color, [0, 0, width, height])
        
    # Fetch the rectangle object that has the dimensions of the image.
    self.rect = self.image.get_rect()
  
  def get_x(self) -> int:
    return self.rect.x
  
  def set_x(self, x: int) -> None:
    self.rect.x = x
  
  def get_y(self) -> int:
    return self.rect.y
  
  def set_y(self, y: int) -> None:
    self.rect.y = y


