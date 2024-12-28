from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
from firebase_admin import credentials, db
from io import BytesIO
from widget_pengajuan_found import *
from chat_found import *

import requests  

def fetch_found_items():
    ref = db.reference('found')
    data = ref.get()
    print(data)  
    return data


def render_found_content(parent_frame, assets_path, user_id):
    ITEMS_PER_PAGE = 2  # Jumlah item per halaman
    current_page = [1]  # Gunakan list agar nilai dapat dimodifikasi dalam fungsi
        
    def update_pagination():
        
        for widget in parent_frame.winfo_children():
            widget.destroy()

        title_label = CTkLabel(
            parent_frame,
            text="Daftar Penemuan Barang",
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
            placeholder_text="Cari barang ditemukan",
            width=380,  
            height=40,  
            border_width=0,
            fg_color="white"  
        )
        entry.place(relx=0.5, rely=0.5, anchor="center")

        button = CTkButton(
            parent_frame,
            text="Ajukan Penemuan Barang",
            font=("Poppins SemiBold", 13),
            command=lambda: render_form(parent_frame, user_id),  
            fg_color="#0067B3"
        )
        button.place(relx=0.8, y=150, anchor="center")
        
        found_items = fetch_found_items()
        if not found_items:
            CTkLabel(
                parent_frame,
                text="Tidak ada data penemuan barang.",
                font=("Poppins SemiBold", 14),
                text_color="#FF0000"
            ).place(relx=0.5, rely=0.6, anchor="center")
            return

        items = list(found_items.items())  
        total_pages = (len(items) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

        start_index = (current_page[0] - 1) * ITEMS_PER_PAGE
        end_index = start_index + ITEMS_PER_PAGE
        page_items = items[start_index:end_index]

        for i, (item_id, item_data) in enumerate(page_items):
            found_frame = CTkFrame(
                parent_frame,
                width=685,
                height=150,
                fg_color="#FFFFFF",
                corner_radius=10
            )
            if i == 0:
                found_frame.pack(pady=(200, 10), padx=45) 
            else:
                found_frame.pack(pady=(20, 10), padx=45)  

                
            rectangle1 = CTkFrame(
                found_frame,
                width=115,
                height=25,
                fg_color="#FFF5D9" if not item_data['is_found'] else "#DCFAF8",  # Warna latar tergantung status
                corner_radius=0
            )
            rectangle1.place(x=550, y=10)  

            
            status_label = CTkLabel(
                rectangle1,
                text="BELUM DIAMBIL PEMILIK" if not item_data['is_found'] else "SUDAH DIAMBIL",
                font=("Poppins SemiBold", 10),
                text_color="#FFBB38" if not item_data['is_found'] else "#16DBCC"
            )
            status_label.place(relx=0.5, rely=0.5, anchor="center")
            
            rectangle2 = CTkFrame(
                found_frame,
                width=1,
                height=85,
                fg_color="#DEDEDE",
                corner_radius=0
            )
            rectangle2.place(x=220, y=40)  

            location_label = CTkLabel(
                found_frame,
                text=f"Lokasi: {item_data['location']}",
                font=("Poppins Regular", 10),
                text_color="#000000"
            )
            location_label.place(x=230, y=50)
            
            
            item_name_label = CTkLabel(
                found_frame,
                text=item_data['name'],
                font=("Poppins SemiBold", 14),
                text_color="#000000"
            )
            item_name_label.place(x=230, y=30)

            description_label = CTkLabel(
                found_frame,
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
                            found_frame,
                            image=CTkImage(light_image=item_image, size=(200, 80)),
                            text=""
                        )
                        item_image_label.place(x=10, y=40)
                    else:
                        print(f"Error: Gambar tidak dapat diambil. Status Code: {response.status_code}")
                except Exception as e:
                    print(f"Error saat mengambil gambar: {e}")

            report_button = CTkButton(
                found_frame,
                text="Sampaikan Kepemilikan Barang",
                font=("Poppins SemiBold", 11),
                fg_color="#7650E1",
                text_color="#FFFFFF",
                width=215,
                height=30,
                corner_radius=5,
                command=lambda item_id=item_id: start_chat(parent_frame, user_id, item_id)
            )
            report_button.place(x=450, y=100)
            
        pagination_frame = CTkFrame(parent_frame, fg_color="#FFFFFF")
        pagination_frame.pack(side="bottom", pady=20)

        if current_page[0] > 1:
            prev_button = CTkButton(
                pagination_frame,
                text="< Previous",
                command=lambda: change_page(-1),
                fg_color="#0067B3"
            )
            prev_button.pack(side="left", padx=5)

        CTkLabel(
            pagination_frame,
            text=f"Page {current_page[0]} of {total_pages}",
            font=("Poppins Regular", 12)
        ).pack(side="left", padx=5)

        if current_page[0] < total_pages:
            next_button = CTkButton(
                pagination_frame,
                text="Next >",
                command=lambda: change_page(1),
                fg_color="#0067B3"
            )
            next_button.pack(side="left", padx=5)

    def change_page(direction):
        current_page[0] += direction
        update_pagination()

    update_pagination()
