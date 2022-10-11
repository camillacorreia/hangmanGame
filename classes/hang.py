import pyglet
from utils import Utils

class Hang:
  def __init__(self):
    self.utils = Utils()

  def draw(self):
    x = self.utils.width // 2 - 300
    y = self.utils.height // 2 - 120

    self.hang = pyglet.graphics.Batch()

    self.hang_1 = pyglet.shapes.Line(x, y, x, y + 300, width=5, batch=self.hang)
    self.hang_2 = pyglet.shapes.Line(
      x, y + 300, x + 100, y + 300, width=5, batch=self.hang
    )
    self.hang_3 = pyglet.shapes.Line(
      x + 100, y + 300, x + 100, y + 270, width=5, batch=self.hang
    )

    self.hang.draw()
