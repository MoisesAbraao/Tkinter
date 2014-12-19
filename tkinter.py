#Tkinter Fenster

from tkinter import *

global rechnen

status = Tk()
status.title("Tkinter Messenger")
status.wm_geometry('500x500+300+400')

class Beispiel:

    def __init__(self, master):
        global rechnen
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="Rechnen==True", command=self.do)
        self.button.pack()
        self.button = Button(frame, text="Rechnen==False", command=self.dont)
        self.button.pack()
        
    def do(self):
        w = Label(status, text="Rechnet...", bg="green", fg="black")
        w.pack(padx=5, pady=10)

    def dont(self):
        w = Label(status, text="Ist faul", bg="red", fg="white")
        w.pack(padx=5, pady=10)


beispiel = Beispiel(status)
status.mainloop()
