from tkinter import *
from tkinter import messagebox, filedialog
from mhmovie.code import *
import os



class app:
    def __init__(self):
        self.window = Tk()
        self.window.title("Audio & Video Mixer")
        self.window.configure(background="gray50")
        self.window.geometry("750x290")

        self.label = Label(self.window, text="NINGÚN ELEMENTO SELECCIONADO", bg="black", width=99, height = 2)
        self.label.place(x=25,y=30)
        self.btnAudio = Button(self.window, text="SELECCIONAR ARCHIVO DE AUDIO", bg="red", fg="white", width=45, height=2, command=self.get_audio)
        self.btnAudio.place(x=25,y=115)
        self.btnVideo = Button(self.window, text="SELECCIONAR ARCHIVO DE VIDEO", bg="red", fg="white", width=45, height=2,command=self.get_video)
        self.btnVideo.place(x=398,y=115)
        self.btnMix = Button(self.window, text="COMBINAR AUDIO Y VIDEO", bg="blue", fg="white", width=98, height=2,command=self.merge)
        self.btnMix.place(x=26,y=200)

        self.window.mainloop()

    def get_audio(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR AUDIO",filetypes =(("mp3 files","*.mp3")
                                          ,("wav files","*.wav"),("mp4 files","*.mp4"),("flv files","*.flv")
                                          ,("ogg files","*.ogg"),("mp2 files","*.mp2"),("aac files","*.aiff")
                                          ,("au files","*.au")))
        if ruta != "":
            aud = (((ruta).split("/"))[-1])
            self.selected_audio = music(aud)

    def get_video(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR AUDIO",filetypes =(("mp4 files","*.mp4"),("AVI files","*.avi")))
        
        if ruta != "":
            vid = (((ruta).split("/"))[-1])
            name, self.vid_ex = os.path.splitext(vid)
            self.selected_video = movie(vid)

    def merge(self):
        try:
            result = self.selected_video + self.selected_audio
            result.save("new_video"+self.vid_ex)
            print("DONE")
        except:
            print("ERROR")


if __name__=="__main__":
    app()


