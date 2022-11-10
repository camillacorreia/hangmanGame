import pyglet
import string
from utils import Utils
from classes.start import Start
from classes.hang import Hang
from classes.gameOver import GameOver

class MainWindow(pyglet.window.Window):
   def __init__(self):
      self.utils = Utils()
      
      super().__init__(self.utils.width, self.utils.height, caption=self.utils.caption, resizable=self.utils.resizable)

      self.start = Start()
      self.gameOver = GameOver()
      self.word, self.tip = self.start.selectWord()
      self.hang = Hang()

   def on_draw(self):
      self.utils.background.blit(0, 0)
      self.hang.draw()
      self.hang.drawHangman(self.word.getWrong())
      self.word.updateLabel()
      self.tip.draw()
      if(self.word.getWrong() > 5):
         self.gameOver.draw(self.word.getCorrectWord())

   def on_key_press(self, symbol, modifiers):
      if chr(symbol) in string.ascii_lowercase:
         self.word.press(chr(symbol))
      if(self.word.getWrong() == 6):
         self.gameOver.press(chr(symbol))
