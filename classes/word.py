import pyglet

class Word:
  def __init__(self, correctWord, window):
    self.wrong = 0 #Quantas vezes o jogador errou

    self.correct = 0 #Quantas vezes o jogador acertou

    self.tried = [] #Quais letras foram tentadas

    self.correctWord = correctWord.lower() #Palavra correta

    self.word = ["_" for letter in self.correctWord] #Palavra que está sendo adivinhada

    self.window = window

    #Labels do jogo
    self.wordLabel = None
    self.triedLabel = None

    self.updateLabel()

  def updateLabel(self):
    self.wordLabel = pyglet.text.Label(
      " ".join(self.word),
      font_name="Config Rounded Bold",
      font_size=56,
      x=self.window.width // 2,
      y=self.window.height // 2 - 120,
    )

    self.triedLabel = pyglet.text.Label(
      " ".join(list(self.tried)),
      font_name="Config Rounded Bold",
      font_size=48,
      color=(255, 46, 52, 255),
      x=self.window.width // 2,
      y=self.window.height // 2 - 220,
      anchor_x="center",
      anchor_y="center",
    )
