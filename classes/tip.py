import pyglet
from utils import Utils

class Tip:
  def __init__(self, tip):
    self.wordTip = tip

  def draw(self):
    x = Utils.WIDTH // 2
    y = Utils.HEIGHT // 2 + 300

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
