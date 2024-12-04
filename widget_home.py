from pathlib import Path
from tkinter import PhotoImage, Canvas
import customtkinter as ctk
from PIL import Image
from firebase_admin import db

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def render_home_content(parent_frame, user_id):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    ref = db.reference(f'users/{user_id}')  
    user_data = ref.get()
    
    if user_data:
        user_name = user_data.get('name', 'Pengguna Tidak Ditemukan')
        user_id_display = user_data.get('id', 'ID Tidak Ditemukan')
        user_nim = user_data.get('username', 'Username Tidak Ditemukan')
    else:
        user_name = 'Pengguna Tidak Ditemukan'
        user_id_display = 'ID Tidak Ditemukan'
        user_nim = 'Username Tidak ditemukan'
    
    # Frame utama untuk area konten
    content_frame = ctk.CTkFrame(
        parent_frame,
        fg_color="#0067B3",
        width=788,
        height=233,
        corner_radius=10
    )
    content_frame.place(x=39, y=134)

    ctk.CTkLabel(
        content_frame,
        text="September 4, 2023",
        font=("Poppins Regular", 16),
        text_color="#FFFFFF"
    ).place(x=28, y=13)

    ctk.CTkLabel(
        content_frame,
        text=f"Selamat Datang, {user_name}, \n NIM {user_nim}",
        font=("Poppins SemiBold", 20),
        text_color="#FFFFFF"
    ).place(x=28, y=40)

    description_text = (
        "Aplikasi SiMALANG memudahkan mahasiswa dan staf ITK\n"
        "dalam melaporkan atau mencari barang hilang dan ditemukan.\n"
        "Pengguna dapat mengunggah data barang serta melihat daftar\n"
        "barang yang terdaftar di sistem."
    )
    ctk.CTkLabel(
        content_frame,
        text=description_text,
        font=("Poppins Regular", 14),
        text_color="#FFFFFF",
        justify="left"
    ).place(x=28, y=120)

    image_path_2 = relative_to_assets("widget_home2.png")
    image2 = ctk.CTkImage(Image.open(image_path_2), size=(320, 258))
    ctk.CTkLabel(content_frame, image=image2, text="").place(x=510, y=15)
    
    # table_frame = ctk.CTkFrame(parent_frame)
    # table_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # # Header Tabel
    # headers = ["No", "Nama", "Kelas", "Nilai"]
    # for col, header in enumerate(headers):
    #     ctk.CTkLabel(table_frame, text=header, width=100, height=30, fg_color="lightblue").grid(row=0, column=col, padx=5, pady=5)

    # # Data Tabel
    # data = [
    #     [1, "Ali", "XII IPA 1", 90],
    #     [2, "Budi", "XII IPA 2", 85],
    #     [3, "Siti", "XII IPA 3", 95]
    # ]

    # # Isi Tabel
    # for row, row_data in enumerate(data, start=1):
    #     for col, item in enumerate(row_data):
    #         ctk.CTkLabel(table_frame, text=item, width=100, height=30, fg_color="white").grid(row=row, column=col, padx=5, pady=5)

