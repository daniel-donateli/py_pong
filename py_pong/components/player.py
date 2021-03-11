from py_pong.components.paddle import Paddle
from py_pong.components.colors import WHITE

class Player:
  def __init__(self, rect_x: int, rect_y: int):
    self.paddle = Paddle(WHITE, 10, 100)
    self.paddle.rect.x = rect_x
    self.paddle.rect.y = rect_y