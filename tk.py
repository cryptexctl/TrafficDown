import os
from tkinter import Tk, Label, Button  # type: ignore

window = Tk()
window.title("TrafficDown | by Sonys9")
window.geometry("300x125")
window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))

statuslbl = Label(window, text="Тут будет статус", font=("Arial Black", 13))
statuslbl.pack()

startbtn = Button(window, text="Начать")
startbtn.pack()
