import random
import json
from classes.word import Word
from classes.tip import Tip

class Start:
  def __init__(self):
    with open("databases/words.json", encoding="utf-8") as databaseWords:
      self.dados = json.load(databaseWords)

  def selectWord(self) -> tuple[Word, Tip]:
    possible: list[dict[str, str]] = []

    for word in self.dados:
      possible.append(word)
 
    selected: dict[str, str] = possible[random.randint(0, len(possible) - 1)]
    selectWord: str = selected["word"]
    selectTip: str = selected["tip"]
   
    return Word(selectWord), Tip(selectTip)
