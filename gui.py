import firebase_admin
import pyrebase
from widget_lost import *
from widget_found import *
from widget_home import *
from firebase_admin import credentials, storage, db
from pathlib import Path
from customtkinter import CTk, CTkLabel, CTkFrame, CTkImage, set_appearance_mode
from PIL import Image
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys

cred = credentials.Certificate('D:/Tubes/Beta V.1/build/lostandfound-78452-firebase-adminsdk-lfwma-f76a4caa1b.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'lostandfound-78452.appspot.com', 
    'databaseURL': 'https://lostandfound-78452-default-rtdb.asia-southeast1.firebasedatabase.app'
})

if len(sys.argv) > 1:
    new_user_id = sys.argv[1]  
else:
    new_user_id = None  # Menangani jika tidak ada argumen


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


set_appearance_mode("light")

window = CTk()
window.geometry("1128x784")
window.configure(bg="#F1F1F1")
window.title("SIMALANG")

canvas = Canvas(
    window,
    bg = "#F1F1F1",
    height = 1024,
    width = 1128,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

sidebar_frame = CTkFrame(
    window,
    width=291,
    height=1024,
    fg_color="#FFFFFF", 
    corner_radius=0
)
sidebar_frame.place(x=0, y=0)

sidebar_title = CTkLabel(
    sidebar_frame,
    text="SIMALANG",
    font=("Poppins SemiBold", 25),
    text_color="#2C2745"
)
sidebar_title.place(x=65, y=28)

menu_items = [
    {"name": "Home", "image": "image_3.png"},
    {"name": "Lost", "image": "image_2.png"},
    {"name": "Found", "image": "image_4.png"},
]

selected_menu = None
menu_frames = {}  
menu_colors = {}

main_frame = CTkFrame(window, width=837, height=1024, fg_color="#F1F1F1", corner_radius=0)
main_frame.place(x=291, y=0)

def render_content(menu_name):
    for widget in main_frame.winfo_children():
        widget.destroy()

    if menu_name == "Home":
        render_home_content(main_frame, new_user_id)
    elif menu_name == "Lost":
        render_lost_content(main_frame, ASSETS_PATH, new_user_id)  
    elif menu_name == "Found":
        render_found_content(main_frame, ASSETS_PATH, new_user_id)  


def select_menu(selected_name):
    global selected_menu
    for name, widgets in menu_frames.items():
        frame, label = widgets
        if name == selected_name:
            menu_colors[name] = "#e6f0f7" 
            frame.configure(fg_color="#e6f0f7")
            label.configure(text_color="#0067B3")  
        else:
            menu_colors[name] = "#FFFFFF"  
            frame.configure(fg_color="#FFFFFF")
            label.configure(text_color="#6E7191")  
    render_content(selected_name)

def on_hover(event, frame, label, menu_name):
    if menu_colors.get(menu_name, "#FFFFFF") != "#e6f0f7":  
        frame.configure(fg_color="#E6E6E6")  
        label.configure(text_color="#000000")  


def on_leave(event, frame, label, menu_name):
    if menu_colors.get(menu_name, "#FFFFFF") != "#e6f0f7":  
        frame.configure(fg_color="#FFFFFF")  
        label.configure(text_color="#6E7191") 

start_y = 112  
for item in menu_items:
    menu_frame = CTkFrame(
        sidebar_frame,
        width=291,
        height=60,
        fg_color="#FFFFFF",
        corner_radius=0
    )
    menu_frame.place(x=0, y=start_y)

    icon_path = relative_to_assets(item["image"])
    icon_image = CTkImage(light_image=Image.open(icon_path), size=(24, 24))
    icon_label = CTkLabel(menu_frame, image=icon_image, text="", fg_color="transparent")
    icon_label.place(x=20, y=18)

    menu_label = CTkLabel(
        menu_frame,
        text=item["name"],
        font=("Poppins Regular", 16),
        text_color="#6E7191",  
    )
    menu_label.place(x=70, y=18)

    menu_colors[item["name"]] = "#FFFFFF"

    menu_frame.bind("<Enter>", lambda e, f=menu_frame, l=menu_label, n=item["name"]: on_hover(e, f, l, n))
    menu_frame.bind("<Leave>", lambda e, f=menu_frame, l=menu_label, n=item["name"]: on_leave(e, f, l, n))
    menu_frame.bind("<Button-1>", lambda e, name=item["name"]: select_menu(name))

    menu_frames[item["name"]] = (menu_frame, menu_label)

    start_y += 60

window.resizable(False, False)

select_menu("Dashboard")

window.mainloop()
