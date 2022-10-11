import pyglet
from utils import Utils

class Tip:
  def __init__(self, tip):
    self.utils = Utils()
    self.wordTip = tip

  def draw(self):
    x = self.utils.width // 2
    y = self.utils.height // 2 + 300

    self.tip = pyglet.text.Label(
      f"Dica: {self.wordTip}",
      font_name="Config Rounded Bold",
      font_size=48,
      color=(59,177,210,255),
      x=x,
      y=y,
      anchor_x="center",
      anchor_y="center",
    )

    self.tip.draw()
