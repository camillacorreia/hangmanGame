import pyglet
from pyglet import shapes

class Hang:
  def __init__(self, window):
    self.window = window
    self.drawHang()

  def drawHang(self):
    x = self.window.width // 2 - 300
    y = self.window.height // 2 - 120

    self.hang = pyglet.graphics.Batch()

    self.hang_1 = shapes.Line(x, y, x, y + 300, width=5, batch=self.hang)
    self.hang_2 = shapes.Line(
      x, y + 300, x + 100, y + 300, width=5, batch=self.hang
    )
    self.hang_3 = shapes.Line(
      x + 100, y + 300, x + 100, y + 270, width=5, batch=self.hang
    )

    self.hang.draw()
