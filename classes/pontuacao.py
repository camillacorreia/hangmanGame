from utils import Utils
import pyglet

#Ao errar uma letra subtrair 10
#Ao acertar uma letra somar 30
#Aparecer a pontuação na tela

class Pontuacao:
    def __init__(self,correct:int,wrong:int):
        self.utils = Utils()
        self.erros = wrong
        self.acertos = correct
        self.pont = 0
    
    

        
    def draw(self):
               

        if((self.erros != 0) or (self.acertos != 0)):
            self.pont = self.pont + ((self.acertos*30) - (self.erros*10))

        if(self.pont < 0):
            self.pont = 0

        self.pontuacao = pyglet.text.Label(
        
            f"Pontos:{str(self.pont)}",
            font_name="Config Rounded Bold",
            font_size=48,
            color=(59,177,210,255),
            x=self.utils.width // 7,
            y=self.utils.height // 5 ,
            anchor_x="center",
            anchor_y="center",
        )
        self.pontuacao.draw()
