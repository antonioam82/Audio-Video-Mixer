from tkinter import *
from mhmovie.code import *

class app:
    def __init__(self):
        self.window = Tk()
        self.window.title("Audio & Video Mixer")
        self.window.configure(background="gray50")
        self.window.geometry("750x290")

        self.label = Label(self.window, text="NINGÚN ELEMENTO SELECCIONADO", bg="black", width=99, height = 2)
        self.label.place(x=25,y=30)
        self.btnAudio = Button(self.window, text="SELECCIONAR ARCHIVO DE AUDIO", bg="red", fg="white", width=45, height=2)
        self.btnAudio.place(x=25,y=115)
        self.btnVideo = Button(self.window, text="SELECCIONAR ARCHIVO DE VIDEO", bg="red", fg="white", width=45, height=2)
        self.btnVideo.place(x=398,y=115)
        self.btnMix = Button(self.window, text="COMBINAR AUDIO Y VIDEO", bg="blue", fg="white", width=98, height=2)
        self.btnMix.place(x=26,y=200)

        self.window.mainloop()


if __name__=="__main__":
    app()

