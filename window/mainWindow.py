import pyglet
import json

file = open('config.json')
data = json.load(file)

caption = data['caption']
width = data['width']
height = data['height']

file.close()

window = pyglet.window.Window(caption=caption, width=width, height=height)
