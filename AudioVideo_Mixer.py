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

        self.window.mainloop()


if __name__=="__main__":
    app()
