import pyglet
import string
from classes.start import Start
from classes.word import Word

logo = pyglet.resource.image("assets/images/icon.png")
background = pyglet.resource.image("assets/images/background.png")

caption = "Hangman Game"
width = 1280
height = 720

window = pyglet.window.Window(caption=caption, width=width, height=height)
window.set_icon(logo)

start = Start(window)

@window.event
def on_draw():
  background.blit(0, 0)
  start.selectWord()

@window.event
def on_key_press(symbol, modifiers):
  if chr(symbol) in string.ascii_lowercase:
    print(chr(symbol))
    Word.press(chr(symbol))
