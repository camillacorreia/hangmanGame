import pyglet
from utils import Utils

class Win:
   def _init_(self):
      self.utils = Utils()

   def draw(self):
      x = self.utils.width
      y = self.utils.height 

      self.win = pyglet.text.Label(
         f"Você venceu! Parabéns!",
         font_name="Config Rounded Bold",
         font_size=50,
         color=(50,205,50),
         x=x,
         y=y,
         anchor_x="center",
         anchor_y="center",
      )

      self.enter = pyglet.text.Label(
         f"Pressione enter para sair",
         font_name="Config Rounded Bold",
         font_size=30,
         color=(255, 255, 255, 255),
         x=x - 130,
         y=y - 400,
         anchor_x="center",
         anchor_y="center",
      )

      self.win.draw()
      self.enter.draw()
      #self.pointGame.draw() Para desenhar futuramente a pontução do jogador
      