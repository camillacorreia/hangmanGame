import pyglet

class Utils(object):
  @property
  def width(self):
    return 1280

  @property
  def height(self):
    return 720

  @property
  def caption(self):
    return "Hangman Game"

  @property
  def resizable(self):
    return False

  @property
  def background(self):
    return pyglet.resource.image("assets/images/background.png")
  
  @property
  def logo(self):
    return pyglet.resource.image("assets/images/icon.png")