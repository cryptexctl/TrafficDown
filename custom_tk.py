import os
from customtkinter import (  # type: ignore
    CTk,
    CTkFrame,
    CTkLabel,
    CTkButton,
    set_appearance_mode,
)

from config import fg, hover, bg

window = CTk()
window.resizable(False, False)
set_appearance_mode("dark")
window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
window.title("TrafficDown | by Sonys9")
window.geometry("300x130")

CTkFrame(window, width=280, height=105).place(x=10, y=10)

statuslbl = CTkLabel(
    window, text="Тут будет статус", font=("Arial Black", 13), bg_color=bg
)
statuslbl.place(relx=0.5, anchor="center", rely=0.25)

CTkLabel(
    window,
    text="Github @Sonys9 | tt @взломщик | tg @freedomleaker2",
    font=("Arial Black", 8),
    bg_color=bg,
).place(x=35, y=108)

startbtn = CTkButton(
    window,
    text="Начать",
    fg_color=fg,
    bg_color=bg,
    hover_color=hover,
)
startbtn.place(x=85, y=70)
