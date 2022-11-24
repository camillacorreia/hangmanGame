import pyglet
from utils import Utils

class Score:
  def __init__(self):
    self.pont: int = 0
    self.countErrors: int = 0
    self.errors: int = 0
    self.hits: int = 0
    self.rightLetters: list[str] = []
    self.countLetter: int = 0
  
  def calculateScore(self, wrong: int, word: str, key: str) -> int:
    cont: int = 0

    for i in word:
      if i == key:
        cont = cont + 1
          
    if cont > 0:
      if key in self.rightLetters:
        self.countLetter = self.countLetter + 0
      else:
        self.rightLetters.append(key)
        self.countLetter = self.countLetter + cont

    self.errors = (wrong - self.countErrors) * 10
    self.hits = self.countLetter * 30

    if self.errors > self.hits:
      self.countErrors = self.countErrors + 1
      self.pont = 0
    else:
      self.pont = self.hits - self.errors

    return self.pont
  
  def draw(self) -> None:
    self.score = pyglet.text.Label(
      f"Pontos: {str(self.pont)}",
      font_name="Config Rounded Bold",
      font_size=44,
      color=(59,177,210,255),
      x=Utils.WIDTH // 6,
      y=Utils.HEIGHT // 5 ,
      anchor_x="center",
      anchor_y="center",
    )

    self.score.draw()
