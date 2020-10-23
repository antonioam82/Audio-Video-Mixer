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
        self.vid = ""
        self.aud = ""

        self.label = Label(self.window, text="NINGÚN ELEMENTO SELECCIONADO", bg="black", fg="red", width=99, height = 2)
        self.label.place(x=25,y=30)
        self.btnAudio = Button(self.window, text="SELECCIONAR ARCHIVO DE AUDIO", bg="red", fg="white",activebackground="white",activeforeground="red",
                               width=45, height=2, command=self.get_audio)
        self.labelT = Label(self.window, bg = "gray50", fg = "white", width = 99, height = 2)
        self.labelT.place(x=25,y=70)
        self.btnAudio.place(x=25,y=115)
        self.btnVideo = Button(self.window, text="SELECCIONAR ARCHIVO DE VIDEO", bg="red", fg="white",activebackground="white",activeforeground="red",
                               width=45, height=2,command=self.get_video)
        self.btnVideo.place(x=398,y=115)
        self.btnMix = Button(self.window, text="COMBINAR AUDIO Y VIDEO", bg="blue", fg="white",activebackground="white",activeforeground="blue",
                             width=98, height=2,command=self.merge)
        self.btnMix.place(x=26,y=200)

        self.window.mainloop()

    def get_audio(self):
        self.labelT.configure(text = "")
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR AUDIO",filetypes =(("wav files","*.wav"),("all files","*")))
        if ruta != "":
            try:
                self.aud = (((ruta).split("/"))[-1])
                print(self.aud)
                if self.vid == "":
                    self.label.configure(text=self.aud)
                else:
                    self.label.configure(text=self.vid+"+"+self.aud)
                self.selected_audio = music(ruta)
            except Exception as e:
                
                messagebox.showwarning("ERROR",str(e))

    def get_video(self):
        self.labelT.configure(text = "")
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR VIDEO",filetypes =(("avi files","*.avi"),("all files","*")))
        if ruta != "":
            try:
                self.vid = (((ruta).split("/"))[-1])
                if self.aud == "":
                    self.label.configure(text=self.vid)
                else:
                    self.label.configure(text=self.aud+"+"+self.vid)
                name, self.vid_ex = os.path.splitext(self.vid)
                self.selected_video = movie(ruta)
            except Exception as e:
                messagebox.showwarning("ERROR",str(e))

    def merge(self):
        if self.vid != "" and self.aud != "":
            new_file=filedialog.asksaveasfilename(initialdir="/",title="Guardar en",defaultextension=self.vid_ex)
            if new_file != "":
                try:
                    video_title = (((new_file).split("/"))[-1])
                    result = self.selected_video + self.selected_audio
                    result.save(new_file)
                    self.labelT.configure(text = "PROCESO FINALIZADO\n ARCHIVO CREADO: "+video_title)
                    print("DONE")
                except:
                    messagebox.showwarning("ERROR","Hubo un error al efectuar la operación")

if __name__=="__main__":
    app()



