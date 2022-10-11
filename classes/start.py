import random
import json
from classes.word import Word
from classes.tip import Tip

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
   
    return Word(selectWord), Tip(selectTip)
