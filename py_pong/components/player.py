from py_pong.components.paddle import Paddle
from py_pong.components.constants import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
  def __init__(self, rect_x: int, rect_y: int):
    self.paddle = Paddle(color = WHITE, width = 10, height = 100)
    self.paddle.rect.x = rect_x
    self.paddle.rect.y = rect_y
    self.score = 0
  
  def move_up(self) -> None:
    self.paddle.set_y(self.paddle.get_y() - 5)
    if self.paddle.get_y() < 0:
      self.paddle.set_y(0)
    
  def move_down(self) -> None:
    self.paddle.set_y(self.paddle.get_y() + 5)
    if self.paddle.get_y() > SCREEN_HEIGHT - 100:
      self.paddle.set_y(SCREEN_HEIGHT - 100)