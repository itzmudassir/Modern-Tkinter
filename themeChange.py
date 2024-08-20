from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.geometry("500x500")

mode = 'dark'

def changeTheme():
    global mode
    if mode == 'dark':
        mode = 'light'
        ctk.set_appearance_mode('light')
    else:
        mode = 'dark'
        ctk.set_appearance_mode('dark')


themeButton = ctk.CTkButton(app, text="Change Theme", command=changeTheme)
themeButton.pack()



app.mainloop()