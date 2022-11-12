from utils import Utils
import pyglet

class Pontuacao:
    def __init__(self):
        self.utils = Utils()
        self.pont = 0
        self.contErros = 0
        self.erros = 0
        self.acertos = 0
        self.LetrasCertas = []
        self.a = 0
    
    
    def CalculaPont(self,wrong:int,palavra:str,key:str):

        cont = 0

        for i in palavra:
            if(i == key):
                cont = cont + 1
              
        if(cont > 0):
            if key in self.LetrasCertas:
                self.a = self.a + 0
            else:
                self.LetrasCertas.append(key)
                self.a = self.a + cont

        self.erros = (wrong - (self.contErros))  *10
        self.acertos = self.a * 30

        if (self.erros > self.acertos):
            self.contErros = self.contErros + 1
            self.pont = 0

        else:
            self.pont = self.acertos - self.erros
        
    def draw(self):
        
        self.pontuacao = pyglet.text.Label(
        
            f"Pontos: {str(self.pont)}",
            font_name="Config Rounded Bold",
            font_size=44,
            color=(59,177,210,255),
            x=self.utils.width // 6,
            y=self.utils.height // 5 ,
            anchor_x="center",
            anchor_y="center",
        )
        self.pontuacao.draw()

