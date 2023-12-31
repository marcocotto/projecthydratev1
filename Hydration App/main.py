import os
import tkinter
import subprocess

import win32gui
import win32con

import customtkinter
from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk, ImageFont

 # Change based on where your folder named Hydration App is located
folder_path = "G:\My Drive\Hydration App"

root = Tk()
root.geometry("495x595")
root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")

root.resizable(width=False, height=False)
root.title("Project Hydrate")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")
    
center_window(root)

def goto_login_window():
    root.destroy()
    subprocess.Popen(["python", "login.py"])
    
def goto_signup_window():
    root.destroy()
    subprocess.Popen(["python", "signup.py"])
     
menu_icon = Image.open(r"" + folder_path + "\Assets\IconMain.png")
waves_bottom = Image.open(r"" + folder_path + "\Assets\WavesFullCropped.png")
title_text_icon = Image.open(r"" + folder_path + "\Assets\TitleText.png")
button_image = Image.open(r"" + folder_path + "\Assets\ButtonImage.png")

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
button_image = button_image.resize((200, 30), resample=Image.BICUBIC)

menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
button_image_tk = ImageTk.PhotoImage(button_image)

menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)

login_button = ttk.Button(root, text="L O G  I N", image=button_image_tk, compound="center", command=goto_login_window)
signup_button = ttk.Button(root, text="S I G N  U P", image=button_image_tk, compound="center", command=goto_signup_window)
signin_options_label = Label(root, text="S I G N  I N  O P T I O N S", fg="darkgray", font=("Arial", 14))

style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)
title_text_label.place(x=153, y=200)

login_button.place(x=140, y=350)
signup_button.place(x=140, y=400)
signin_options_label.place(x=130, y=310)

title_text_label.lower(login_button)
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop()