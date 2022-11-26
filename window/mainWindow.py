import pyglet
import string
from utils import Utils
from classes.start import Start
from classes.hang import Hang
from classes.gameOver import GameOver

class MainWindow(pyglet.window.Window):
   def __init__(self):
      super().__init__(Utils.WIDTH, Utils.HEIGHT, caption=Utils.CAPTION, resizable=Utils.RESIZABLE)
      
      self.start: Start = Start()
      self.gameOver = GameOver()
      self.word, self.tip = self.start.selectWord()
      self.hang: Hang = Hang()

   def on_draw(self) -> None:
      Utils.BACKGROUND.blit(0, 0)
      self.hang.draw()
      self.hang.drawHangman(self.word.getWrong())
      self.word.updateLabel()
      self.tip.draw()
      if(self.word.getWrong() > 5):
         self.gameOver.draw(self.word.getCorrectWord())
      ## self.winner.draw()
      ## self.loser.draw()

   def on_key_press(self, symbol, modifiers) -> None:
      if chr(symbol) in string.ascii_lowercase:
         self.word.press(chr(symbol))
      if(self.word.getWrong() == 6):
         self.gameOver.press(chr(symbol))
