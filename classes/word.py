import pyglet
from utils import Utils
from classes.score import Score
from classes.winner import Winner
from classes.gameOver import GameOver

class Word:
  def __init__(self, correctWord: str):

    self.wrong: int = 0 #Quantas vezes o jogador errou

    self.correct: int = 0 #Quantas vezes o jogador acertou

    self.tried: list[str] = [] #Quais letras foram tentadas

    self.correctWord: str = correctWord.lower() #Palavra correta

    self.word: str = ["_" for letter in self.correctWord] #Palavra que está sendo adivinhada

    self.score: Score = Score()

    self.winner: Winner = Winner()

    self.gameOver: GameOver = GameOver()
    
    self.errors: int = 0 

    #Labels do jogo
    self.wordLabel = None
    self.triedLabel = None

  def updateLabel(self) -> None:
    self.wordLabel = pyglet.text.Label(
      " ".join(self.word),
      font_name="Config Rounded Bold",
      font_size=56,
      x=Utils.WIDTH // 2,
      y=Utils.HEIGHT // 2 - 120,
    )

    self.wordLabel.draw()
    self.score.draw()

    self.triedLabel = pyglet.text.Label(
      " ".join(list(self.tried)),
      font_name="Config Rounded Bold",
      font_size=48,
      color=(255, 46, 52, 255),
      x=Utils.WIDTH // 2,
      y=Utils.HEIGHT // 2 - 220,
      anchor_x="center",
      anchor_y="center",
    )

    self.triedLabel.draw()
 
  def press(self, key: str) -> None:
    if self.wrong <= 5:
      found: bool = False

      for i in range(len(self.correctWord)):
        if self.correctWord[i] == key:
          self.word[i] = key
          found = True
          self.correct += 1

      if not found:
        if key not in self.tried:
          self.tried.append(key)
          self.errors += 1
        self.wrong += 1
      
      self.updateLabel()
      self.score.calculateScore(self.errors, self.correctWord, key)

  def drawWinner(self) -> bool:
    flagWinner: bool = False

    if self.correct == len(self.correctWord):
      self.tried = []
      self.word = []

      self.winner.draw(self.correctWord)
      flagWinner = True

    return flagWinner
   
  def drawLoser(self) -> bool:
    flagLoser: bool = False

    if self.wrong > 5:
      self.tried = []
      self.word = []

      self.gameOver.draw(self.correctWord)
      flagLoser = True
    
    return flagLoser
  
  def getWrong(self) -> int:
    return self.wrong
