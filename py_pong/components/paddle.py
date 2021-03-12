import pygame
from py_pong.components.constants import BLACK

class Paddle(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    # Call the parent class (Sprite) constructor
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
  
  def get_x(self):
    return self.rect.x
  
  def set_x(self, x: int):
    self.rect.x = x
  
  def get_y(self):
    return self.rect.y
  
  def set_y(self, y: int):
    self.rect.y = y


