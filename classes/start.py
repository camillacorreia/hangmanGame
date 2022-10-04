from classes.word import Word
from classes.hang import Hang

import random
import json

class Start:
  def __init__(self, window):
    self.window = window
    with open("databases/words.json", encoding='utf-8') as databaseWords:
      self.dados = json.load(databaseWords)

  def selectWord(self):
    possible = []

    for i in self.dados:
      possible.append(i)
  
    selected = possible[random.randint(0, len(possible) - 1)]
    selectTip = selected['tip']
    selectWord = selected['word']

    print(selectWord, selectTip)
    
    word = Word(selectWord, self.window)
    word.wordLabel.draw()

    hang = Hang(self.window)
    hang.draw_hang()
       