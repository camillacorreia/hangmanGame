import pyglet
import json

file = open('config.json')
data = json.load(file)

caption = data['CAPTION']
width = data['WIDTH']
height = data['HEIGHT']

file.close()

window = pyglet.window.Window(caption=caption, width=width, height=height)
