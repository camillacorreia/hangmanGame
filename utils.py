import pyglet
from typing import Any

class Utils:
  CAPTION: str = "Hangman Game"
  WIDTH: int = 1280
  HEIGHT: int = 720
  RESIZABLE: bool = False
  LOGO: Any = pyglet.resource.image("assets/images/icon.png")
  BACKGROUND: Any = pyglet.resource.image("assets/images/background.png")
