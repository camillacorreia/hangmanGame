from classes.word import Word

import random
import json

class Start:
  def __init__(self):
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
   
    # Chamar a classe dica Tip(selectTip)
    return Word(selectWord)    