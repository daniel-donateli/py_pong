import pygame
from typing import Tuple
from random import randint
from py_pong.components.constants import BLACK

class Ball(pygame.sprite.Sprite):
  def __init__(self, color: Tuple[int, int, int], width: int, height: int):
    # Call Sprite constructor
    super().__init__()

    # Pass in the color of the ball, its width and height.
    # Set the background color and set it to be transparent
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
 
    # Draw the ball
    pygame.draw.rect(self.image, color, [0, 0, width, height])
        
    self.velocity = [randint(4,8),randint(-8,8)]
        
    # Fetch the rectangle object that has the dimensions of the image.
    self.rect = self.image.get_rect()
  
  def update(self):
    # Increment current x, y positions by velocity
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
  
  def bounce(self):
    self.velocity[0] = -self.velocity[0]
    self.velocity[1] = randint(-8,8)