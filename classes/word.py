import pyglet
from utils import Utils
from classes.score import Score
from classes.winner import Winner
from classes.gameOver import GameOver


class Word:
    def __init__(self, correctWord: str):

        self.__wrong: int = 0  # Quantas vezes o jogador errou

        self.__correct: int = 0  # Quantas vezes o jogador acertou

        self.tried: list[str] = []  # Quais letras foram tentadas

        self.correctWord: str = correctWord.lower()  # Palavra correta

        self.word: str = ["_" for letter in self.correctWord]  # Palavra que está sendo adivinhada

        self.score: Score = Score()

        self.winner: Winner = Winner()

        self.gameOver: GameOver = GameOver()

        # Labels do jogo
        self.wordLabel = None
        self.triedLabel = None

    def set_wrong(self):
        self.__wrong += 1

    def set_correct(self):
        self.__correct += 1

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
         if self.__wrong <= 5:
               found: bool = False

               for i in range(len(self.correctWord)):
                  if self.correctWord[i] == key:
                     self.word[i] = key
                     found = True
                     self.set_correct()

               if not found:
                  if key not in self.tried:
                     self.tried.append(key)
                     self.set_wrong()

               self.updateLabel()
               self.score.calculateScore(self.__wrong, self.correctWord, key)

    def drawWinner(self) -> bool:
        flagWinner: bool = False

        if self.__correct == len(self.correctWord):
            self.tried = []
            self.word = []

            self.winner.draw(self.correctWord)
            flagWinner = True

        return flagWinner

    def drawLoser(self) -> bool:
        flagLoser: bool = False

        if self.__wrong > 5:
            self.tried = []
            self.word = []

            self.gameOver.draw(self.correctWord)
            flagLoser = True

        return flagLoser

    def getWrong(self) -> int:
        return self.__wrong