import pyglet
import string
from utils import Utils
from classes.start import Start
from classes.hang import Hang

class MainWindow(pyglet.window.Window):
  def __init__(self):
    utils = Utils()
    super().__init__(utils.width, utils.height, caption=utils.caption, resizable=utils.resizable)
    self.utils = utils
    self.start = Start()
    self.word = self.start.selectWord()
    self.hang = Hang()

  def on_draw(self):
    self.utils.background.blit(0, 0)
    self.hang.draw()
    self.word.updateLabel()
    self.word.drawHangman()
    ## self.word.drawWinner()
    ## self.word.drawLoser()

  def on_key_press(self, symbol, modifiers):
    if chr(symbol) in string.ascii_lowercase:
      print(chr(symbol))
      self.word.press(chr(symbol))
