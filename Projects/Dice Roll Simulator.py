from tkinter import *
import random

root = Tk()
root.geometry("600x400")
root.title("Dice Roll Simulator")

label = Label(root, text="", font=("aerial", 200))


def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()


button = Button(root, text="Let's Roll ....", width=30, height=3, font=6, bg="white", bd=2, command=roll)
button.pack(padx=3, pady=3)
root.mainloop()

