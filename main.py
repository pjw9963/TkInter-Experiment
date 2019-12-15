import tkinter as tk
from playsound import playsound


soundbit = 'daddy.wav'

def play_bit():
    playsound(soundbit)

root = tk.Tk()
root.geometry("600x400")
root.title("My Project")

button = tk.Button(root, text='Quote Arnold', bg="#3f3f8f", fg='white', activebackground='#6b6bc9', activeforeground="white", command=play_bit)
button.pack()

label = tk.Label(root, text="Hello World")
label.pack(padx=20, pady=20)

root.mainloop()
