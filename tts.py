import tkinter as tk
import pyttsx3 

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.configure(background="pink")
        self.root.resizable(0,0)
        self.label = tk.Label(self.root, bg="pink", fg="brown", font="Arial 25 bold", text="What do you want me to speak")
        self.label.pack()
        self.textbox = tk.Entry(self.root, width= 35, font="Arial 20")
        self.textbox.pack()
        self.button = tk.Button(self.root, bg= "red", width=5, font="Arial 15 bold", text= "Speak!")
        self.button.pack() 
        self.root.mainloop()

if __name__ == "__main__":
    temp = Widget()