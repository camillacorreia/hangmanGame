import pyglet
from classes.start import Start

logo = pyglet.resource.image("assets/images/icon.png")
background = pyglet.resource.image("assets/images/background.png")

caption = "Hangman Game"
width = 1280
height = 720

window = pyglet.window.Window(caption=caption, width=width, height=height)
window.set_icon(logo)
background.blit(0, 0)

start = Start(window)
start.selectWord()
