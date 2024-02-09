import PySimpleGUI as sg
from PIL import Image

image = Image.open('melilla.png')

new_size = (1920, 1080)
resized = image.resize(new_size)
resized.save('melilla_small.png')
resized

layout = [
    [sg.Image(filename='melilla_small.png')], #expand_x=True, expand_y=True
    #[sg.Button(image_source='image.png')],
]

window = sg.Window("IMG", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
