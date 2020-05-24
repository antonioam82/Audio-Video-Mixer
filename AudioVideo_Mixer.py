from tkinter import *
from tkinter import messagebox, filedialog
from mhmovie.code import *
import os
#import glob

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
        self.btnAudio = Button(self.window, text="SELECCIONAR ARCHIVO DE AUDIO", bg="red", fg="white", width=45, height=2, command=self.get_audio)
        self.btnAudio.place(x=25,y=115)
        self.btnVideo = Button(self.window, text="SELECCIONAR ARCHIVO DE VIDEO", bg="red", fg="white", width=45, height=2,command=self.get_video)
        self.btnVideo.place(x=398,y=115)
        self.btnMix = Button(self.window, text="COMBINAR AUDIO Y VIDEO", bg="blue", fg="white", width=98, height=2,command=self.merge)
        self.btnMix.place(x=26,y=200)

        self.window.mainloop()

    def get_audio(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR AUDIO",filetypes =(("wav files","*.wav"),("all files","*")))
        if ruta != "":
            try:
                self.aud = (((ruta).split("/"))[-1])
                if self.vid == "":
                    self.label.configure(text=self.aud)
                else:
                    self.label.configure(text=self.vid+"+"+self.aud)
                self.selected_audio = music(self.aud)
            except:
                messagebox.showwarning("ERROR","Archivo no válido")

    def get_video(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR VIDEO",filetypes =(("avi files","*.avi"),("all files","*")))
        if ruta != "":
            try:
                self.vid = (((ruta).split("/"))[-1])
                if self.aud == "":
                    self.label.configure(text=self.vid)
                else:
                    self.label.configure(text=self.aud+"+"+self.vid)
                name, self.vid_ex = os.path.splitext(self.vid)
                self.selected_video = movie(self.vid)
            except:
                messagebox.showwarning("ERROR","Archivo no válido")

    def merge(self):
        if self.vid != "" and self.aud != "":
            try:
                new_file=filedialog.asksaveasfilename(initialdir="/",title="Guardar en",defaultextension=".avi")
                if new_file != "":
                    result = self.selected_video + self.selected_audio
                    result.save(new_file)
                    #print(os.getcwd())
                    #video_name = self.file_name()
                    #result.save(video_name)
                    print("DONE")
            except:
                messagebox.showwarning("ERROR","Hubo un error al efectuar la operación")


    #def file_name(self):
        #count = 0
        #for i in glob.glob("*"+self.vid_ex):
            #if "mixed_video" in i:
                #count+=1
        #if count>0:
            #name = "mixed_video"+"("+str(count)+")"+self.vid_ex
        #else:
            #name = "mixed_video"+self.vid_ex
        #return name"""

if __name__=="__main__":
    app()




