import pyglet
from utils import Utils

class Hang:
  def draw(self) -> None:
    x: int = Utils.WIDTH // 2 - 300
    y: int = Utils.HEIGHT // 2 - 120

    self.hang = pyglet.graphics.Batch()

    self.hang_1 = pyglet.shapes.Line(x, y, x, y + 300, width=5, batch=self.hang)
    self.hang_2 = pyglet.shapes.Line(
      x, y + 300, x + 100, y + 300, width=5, batch=self.hang
    )
    self.hang_3 = pyglet.shapes.Line(
      x + 100, y + 300, x + 100, y + 270, width=5, batch=self.hang
    )

    self.hang.draw()
  
  def drawHangman(self, wrong: int) -> None:
    x: int = Utils.WIDTH // 2 - 200
    y: int = Utils.HEIGHT // 2 + 120

    self.hangman = pyglet.graphics.Batch()

    if wrong > 0:
      self.head = pyglet.shapes.Circle(
        x, y, 30, color=(255, 255, 255), batch=self.hangman
    )

    if wrong > 1:
      self.body = pyglet.shapes.Line(x, y, x, y - 120, width=5, batch=self.hangman)

    if wrong > 2:
      self.arm_1 = pyglet.shapes.Line(
        x, y - 50, x - 40, y - 100, width=5, batch=self.hangman
      )

    if wrong > 3:
      self.arm_2 = pyglet.shapes.Line(
        x, y - 50, x + 40, y - 100, width=5, batch=self.hangman
      )

    if wrong > 4:
      self.leg_1 = pyglet.shapes.Line(
        x, y - 120, x - 40, y - 200, width=5, batch=self.hangman
      )

    if wrong > 5:
      self.leg_2 = pyglet.shapes.Line(
        x, y - 120, x + 40, y - 200, width=5, batch=self.hangman
      )

    self.hangman.draw()
