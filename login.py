import pyrebase
import firebase_admin
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from firebase_admin import credentials, firestore, auth
import subprocess  
import os

# Initialize Firebase Admin
cred = credentials.Certificate('D:/Tubes/Beta V.1/build/lostandfound-78452-firebase-adminsdk-lfwma-f76a4caa1b.json')
firebase_admin.initialize_app(cred)

def login_with_google():
    try:
        credentials_path = "client_secret_397750283025-8gl75si6f9ictssmrsc4f478de7t7l2s.apps.googleusercontent.com.json"  # Update path as needed
        SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'openid']

        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=8080)  

        id_token = creds.id_token  

    
        if decoded_token['aud'] != 'lostandfound-78452':  # Your Firebase project ID
            raise Exception("Audience claim in ID token is invalid!")

        email = decoded_token['email']  

        if "@student.itk.ac.id" not in email:
            messagebox.showerror("Error", "Only @student.itk.ac.id email addresses are allowed.")
            return

        db = firestore.client()
        users_ref = db.collection('users')

        user_doc = users_ref.where('email', '==', email).get()
        if len(user_doc) == 0:
            username = email.split('@')[0]  
            users_ref.add({
                'username': username,
                'email': email
            })

        messagebox.showinfo("Success", f"Login successful as {email}.")
        subprocess.run(["python", "gui.py"])  

    except Exception as e:
        messagebox.showerror("Error", f"Login failed: {str(e)}")

# def login_with_google():
#     try:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             'client_secret_397750283025-8gl75si6f9ictssmrsc4f478de7t7l2s.apps.googleusercontent.com.json',
#             scopes=['https://www.googleapis.com/auth/userinfo.email', 'openid']
#         )

#         credentials = flow.run_local_server(port=8080, open_browser=True)

#         id_token = credentials.id_token

#         user = auth.sign_in_with_custom_token(id_token)
#         user_info = auth.get_account_info(user['idToken'])

#         email = user_info['users'][0]['email']
        
#         if "@student.itk.ac.id" not in email:
#             messagebox.showerror("Error", "Hanya email @student.itk.ac.id yang diizinkan.")
#             return

    #     db = firestore.client()
    #     users_ref = db.collection('users')
        
    #     user_doc = users_ref.where('email', '==', email).get()
    #     if len(user_doc) == 0:
    #         username = email.split('@')[0]  
    #         users_ref.add({
    #             'username': username,
    #             'email': email
    #         })

    #     messagebox.showinfo("Success", f"Login berhasil sebagai {email}.")
    #     subprocess.run(["python", "gui.py"])  

    # except Exception as e:
    #     messagebox.showerror("Error", f"Gagal login: {str(e)}")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Tubes\Login\build\assets\frame0")


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
    file=relative_to_assets("image_1.png"))
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
    text="OR",
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
    file=relative_to_assets("image_2.png"))
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
    file=relative_to_assets("image_3.png"))
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
    file=relative_to_assets("button_1.png"))
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
    file=relative_to_assets("image_4.png"))
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
