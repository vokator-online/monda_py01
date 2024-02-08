import PySimpleGUI as sg

layout = [
    [sg.Image(filename='image.png')], #expand_x=True, expand_y=True
    #[sg.Button(image_source='image.png')],
]

window = sg.Window("IMG", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
