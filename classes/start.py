from classes.word import Word
from classes.hang import Hang

import random
import json
import string

class Start:
  def __init__(self, window):
    self.window = window
    with open("databases/words.json", encoding='utf-8') as databaseWords:
      self.dados = json.load(databaseWords)

  def selectWord(self):
    possible = []

    for word in self.dados:
      possible.append(word)
  
    selected = possible[random.randint(0, len(possible) - 1)]
    selectWord = selected['word']
    selectTip = selected['tip']

    print(selectWord, selectTip)
    
    Word(selectWord, self.window)
    # Chamar a classe dica Tip(selectTip, self.window)
    Hang(self.window)
       