import pyglet
import string
from utils import Utils
from classes.start import Start
from classes.hang import Hang

class MainWindow(pyglet.window.Window):
  def __init__(self):
    self.utils = Utils()
    
    super().__init__(self.utils.width, self.utils.height, caption=self.utils.caption, resizable=self.utils.resizable)
    
    self.start = Start()
    self.word, self.tip = self.start.selectWord()
    self.hang = Hang()

  def on_draw(self):
    self.utils.background.blit(0, 0)
    self.hang.draw()
    self.hang.drawHangman(self.word.getWrong())
    self.word.updateLabel()
    self.tip.draw()
    ## self.winner.draw()
    ## self.loser.draw()

  def on_key_press(self, symbol, modifiers):
    if chr(symbol) in string.ascii_lowercase:
      self.word.press(chr(symbol))
