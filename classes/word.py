from utils import Utils
import pyglet
from classes.gameOver import GameOver

utils = Utils()

class Word:
   def __init__(self, correctWord):

      self.wrong = 0 #Quantas vezes o jogador errou

      self.correct = 0 #Quantas vezes o jogador acertou

      self.tried = [] #Quais letras foram tentadas

      self.correctWord = correctWord.lower() #Palavra correta

      self.word = ["_" for letter in self.correctWord] #Palavra que está sendo adivinhada

      #Labels do jogo
      self.wordLabel = None
      self.triedLabel = None

   def updateLabel(self):
      self.wordLabel = pyglet.text.Label(
         " ".join(self.word),
         font_name="Config Rounded Bold",
         font_size=56,
         x=utils.width // 2,
         y=utils.height // 2 - 120,
      )

      self.wordLabel.draw()

      self.triedLabel = pyglet.text.Label(
         " ".join(list(self.tried)),
         font_name="Config Rounded Bold",
         font_size=48,
         color=(255, 46, 52, 255),
         x=utils.width // 2,
         y=utils.height // 2 - 220,
         anchor_x="center",
         anchor_y="center",
      )

      self.triedLabel.draw()
   
   def press(self, key):
      if self.wrong <= 5:
         found = False
         for i in range(len(self.correctWord)):
            if self.correctWord[i] == key:
               self.word[i] = key
               found = True
               self.correct += 1

         if not found:
            if key not in self.tried:
               self.tried.append(key)
            self.wrong += 1

         self.updateLabel()

   def drawWinner(self):
      if self.correct == len(self.correctWord):
         self.tried = []
         self.word = []

         #Chamar a Classe Winner(self.correctWord)
         self.updateLabel()
      
   def drawLoser(self):
      if self.wrong > 5:
         self.tried = []
         self.word = []

         #Chamar a Classe Loser(self.correctWord) // Mostrar qual a palavra correta
         self.updateLabel()
   
   def getWrong(self):
      return self.wrong

   def getCorrectWord(self):
      return self.correctWord
