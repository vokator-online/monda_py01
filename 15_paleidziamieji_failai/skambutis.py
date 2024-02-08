import PySimpleGUI as sg
import pygame

def skambutis(skambutis_failas):
    pygame.init()
    pygame.mixer.music.load(skambutis_failas)
    pygame.mixer.music.play()

if __name__ == "__main__":
    skambutis_failas = "skambutis.mp3"

    image_layout = [
        [sg.Image(filename='skambutis.png')],
    ]

    image_window = sg.Window("IMG", image_layout, resizable=True)

    skambutis(skambutis_failas)

    while True:
        event, values = image_window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if not pygame.mixer.music.get_busy():
            break

    image_window.close()
    pygame.quit()
