from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
import firebase_admin
from firebase_admin import credentials, db
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
from io import BytesIO

import requests  # Tambahkan ini jika menggunakan gambar dari URL

# cred = credentials.Certificate('D:/Tubes/GuiPengajuan/build/lostandfound-78452-firebase-adminsdk-lfwma-f76a4caa1b.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'lostandfound-78452.appspot.com',
#     'databaseURL': 'https://lostandfound-78452-default-rtdb.asia-southeast1.firebasedatabase.app'
# })


def fetch_lost_items():
    ref = db.reference('lost')
    data = ref.get()
    print(data)  
    return data


def render_lost_content(parent_frame,  assets_path):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    title_label = CTkLabel(
        parent_frame,
        text="Daftar Barang Hilang",
        font=("Poppins SemiBold", 30),
        text_color="#353E6C"
    )
    title_label.place(relx=0.26, y=120, anchor="center")

    rounded_frame = CTkFrame(
        parent_frame,
        fg_color="#f0f0f0",  
        corner_radius=24,     
        width=420,
        height=60
    )
    rounded_frame.place(relx=0.28, y=50, anchor="center")

    entry = CTkEntry(
        rounded_frame,
        placeholder_text="Cari barang hilang",
        width=380,  
        height=40,  
        border_width=0,
        fg_color="white"  
    )
    entry.place(relx=0.5, rely=0.5, anchor="center")

    button = CTkButton(
        parent_frame,
        text="Ajukan Kehilangan Barang",
        font=("Poppins SemiBold", 13),
        command=lambda: print("Ajukan Kehilangan clicked"),
        fg_color="#0067B3"
    )
    button.place(relx=0.8, y=150, anchor="center")
    
    lost_items = fetch_lost_items()
    if isinstance(lost_items, dict):
        item_data = lost_items

    if not lost_items:
        CTkLabel(
            parent_frame,
            text="Tidak ada data barang hilang.",
            font=("Poppins SemiBold", 14),
            text_color="#FF0000"
        ).place(relx=0.5, rely=0.6, anchor="center")
        return

    for i, (item_id, item_data) in enumerate(lost_items.items()):
        if isinstance(item_data, dict):  
            print(f"Valid data: {item_data}")
        else:
            print(f"Invalid format: {item_data}")  
        lost_frame = CTkFrame(
            parent_frame,
            width=685,
            height=150,
            fg_color="#FFFFFF",
            corner_radius=10
        )
        if i == 0:
            lost_frame.pack(pady=(200, 10), padx=45) 
        else:
            lost_frame.pack(pady=(20, 10), padx=45)  

            
        rectangle1 = CTkFrame(
            lost_frame,
            width=115,
            height=25,
            fg_color="#FFF5D9",
            corner_radius=0
        )
        rectangle1.place(x=550, y=10)  

        # status_label = CTkLabel(
        #     rectangle1,
        #     text="BELUM DITEMUKAN",
        #     font=("Poppins SemiBold", 10),
        #     text_color="#FFBB38"
        # )
        # # Posisi tetap relatif terhadap rectangle1
        # status_label.place(relx=0.5, rely=0.5, anchor="center")
        
        
        status_label = CTkLabel(
            rectangle1,
            text="BELUM DITEMUKAN" if not item_data['is_found'] else "DITEMUKAN",
            font=("Poppins SemiBold", 10),
            text_color="#FFBB38" if not item_data['is_found'] else "#00FF00"
        )
        status_label.place(relx=0.5, rely=0.5, anchor="center")
        
        rectangle2 = CTkFrame(
            lost_frame,
            width=1,
            height=85,
            fg_color="#DEDEDE",
            corner_radius=0
        )
        rectangle2.place(x=220, y=40)  

        location_label = CTkLabel(
            lost_frame,
            text=f"Lokasi: {item_data['location']}",
            font=("Poppins Regular", 10),
            text_color="#000000"
        )
        location_label.place(x=230, y=50)
        
        
        item_name_label = CTkLabel(
            lost_frame,
            text=item_data['name'],
            font=("Poppins SemiBold", 14),
            text_color="#000000"
        )
        item_name_label.place(x=230, y=30)

        description_label = CTkLabel(
            lost_frame,
            text=item_data['description'],
            font=("Poppins Regular", 10),
            text_color="#000000",
            justify="left"
        )
        description_label.place(x=230, y=70)

    if 'images' in item_data:
        try:
            image_url = item_data['images']
            response = requests.get(image_url, stream=True)
            
            if response.status_code == 200:
                item_image = Image.open(BytesIO(response.content))
                item_image = item_image.resize((200, 80))  
                
                item_image_label = CTkLabel(
                    lost_frame,
                    image=CTkImage(light_image=item_image, size=(200, 80)),
                    text=""
                )
                item_image_label.place(x=10, y=40)
            else:
                print(f"Error: Gambar tidak dapat diambil. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error saat mengambil gambar: {e}")

        report_button = CTkButton(
            lost_frame,
            text="Sampaikan Penemuan Barang",
            font=("Poppins SemiBold", 11),
            fg_color="#7650E1",
            text_color="#FFFFFF",
            width=215,
            height=30,
            corner_radius=5,
            command=lambda: print("Report button clicked")
        )
        report_button.place(x=450, y=100)