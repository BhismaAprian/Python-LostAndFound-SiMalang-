import firebase_admin
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from firebase_admin import credentials, firestore, auth, db
import subprocess  
import requests
import customtkinter as ctk
import threading
import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))  
cred_path = os.path.join(base_dir, 'cred/lostandfound-78452-firebase-adminsdk-lfwma-f76a4caa1b.json')

API_KEY = "AIzaSyDDhFEVpqjSYbjVhbOj5AwlmmVavC868pM"  
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'lostandfound-78452.appspot.com', 
    'databaseURL': 'https://lostandfound-78452-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def show_popup(title, message, popup_type="success"):
    popup = ctk.CTkToplevel()
    popup.geometry("300x200")
    popup.title(title)
    popup.grab_set()

    colors = {"success": "green", "error": "red", "info": "blue"}
    bg_color = colors.get(popup_type, "gray")

    header = ctk.CTkLabel(popup, text=title, font=("Arial", 18, "bold"), fg_color=bg_color, text_color="white")
    header.pack(fill="x", pady=(0, 10))

    message_label = ctk.CTkLabel(popup, text=message, font=("Arial", 14), wraplength=250)
    message_label.pack(pady=20)

    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy, fg_color="gray")
    close_button.pack(pady=10)

    for i in range(0, 101, 5):
        popup.attributes("-alpha", i / 100)
        popup.update()
        popup.after(10)
        
def login_with_google():
    try:
        credentials_path = os.path.join(base_dir, "cred/client_secret_397750283025-8gl75si6f9ictssmrsc4f478de7t7l2s.apps.googleusercontent.com.json")
        SCOPES = [
            'https://www.googleapis.com/auth/userinfo.profile',
            'https://www.googleapis.com/auth/userinfo.email',
            'openid'
        ]
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=8080)

        id_token = creds.id_token

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={API_KEY}"

        payload = {
            "postBody": f"id_token={id_token}&providerId=google.com",
            "requestUri": "http://localhost",
            "returnSecureToken": True
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if response.status_code == 200:
            email = data['email']
            name = data['fullName']

            if "@student.itk.ac.id" not in email:
                show_popup("Error", "Hanya Email @student.itk.ac.id Saja yang diizinkan.", "error")
                return

            username = email.split('@')[0]
            users_ref = db.reference('users')
            new_user_id = 2
            user_doc = users_ref.order_by_child('email').equal_to(email).get()
            if not user_doc:
                users_ref.child(str(new_user_id)).set({
                    'id': new_user_id,
                    'name': name,
                    'username': username,
                    'email': email
                })

            show_popup("Success", f"Login Berhasil as {email} , {name} .", "success")

            threading.Thread(target=run_gui, args=(new_user_id,)).start()

        else:
            show_popup("Error", f"Login failed: {data.get('error', {}).get('message', 'Unknown error')}", "error")

    except Exception as e:
        show_popup("Error", f"Login failed: {str(e)}", "error")

def run_gui(user_id):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  
        gui_path = os.path.join(base_dir, "widgets", "gui.py")
        
        subprocess.run(["python", gui_path, str(user_id)])
    except Exception as e:
        print(f"Error running GUI: {e}")
def close_login():
    window.destroy()

        
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1248x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1248,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("itk.png"))
image_1 = canvas.create_image(
    150.0,
    450.0,
    image=image_image_1
)

canvas.create_rectangle(
    594.0,
    0.0,
    1248.0,
    815.0,
    fill="#D8D7D7",
    outline="")

canvas.create_text(
    638.0,
    67.0,
    anchor="nw",
    text="Welcome to\n",
    fill="#2E2E2E",
    font=("Poppins Medium", 36 * -1)
)

canvas.create_rectangle(
    634.0,
    223.0,
    1208.0,
    305.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    638.0,
    110.0,
    anchor="nw",
    text="SIMALANG",
    font=("Poppins SemiBold", 40),
    fill="#0067B3",
)

canvas.create_text(
    890.0,
    255.0,
    anchor="nw",
    text="Login with Google",   
    fill="#2E2E2E",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_rectangle(
    646.0,
    339.0,
    892.0,
    340.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    969.0,
    338.9999748126229,
    1213.0,
    340.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    922.0,
    329.0,
    anchor="nw",
    text="---",
    fill="#FFFFFF",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_rectangle(
    654.0,
    387.0,
    1213.0,
    464.0,
    fill="#EBEBEB",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("email.png"))
image_2 = canvas.create_image(
    685.0,
    430.0,
    image=image_image_2
)

canvas.create_text(
    722.0,
    402.0,
    anchor="nw",
    text="Email",
    fill="#2E2E2E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    722.0,
    424.0,
    anchor="nw",
    text="example@gmail.com",
    fill="#2E2E2E",
    font=("Poppins", 16 * -1)
)

canvas.create_rectangle(
    654.0,
    484.0,
    1213.0,
    561.0,
    fill="#EBEBEB",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("key.png"))
image_3 = canvas.create_image(
    685.0,
    529.0,
    image=image_image_3
)

canvas.create_text(
    730.0,
    499.0,
    anchor="nw",
    text="Password",
    fill="#2E2E2E",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    730.0,
    527.0,
    anchor="nw",
    text="***********",
    fill="#2E2E2E",
    font=("Poppins", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login_with_google,
    relief="flat"
)
button_1.place(
    x=644.0,
    y=643.0,
    width=569.0,
    height=77.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("google.png"))
image_4 = canvas.create_image(
    865.0,
    264.0,
    image=image_image_4
)

canvas.create_text(
    909.0,
    670.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
