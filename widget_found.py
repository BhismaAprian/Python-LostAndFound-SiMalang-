from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image

def render_found_content(parent_frame,  assets_path):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    title_label = CTkLabel(
        parent_frame,
        text="Daftar Penemuan Barang",
        font=("Poppins SemiBold", 30),
        text_color="#353E6C"
    )
    title_label.place(relx=0.3, y=120, anchor="center")

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
        command=lambda: print("Ajukan Penemuan clicked"),
        fg_color="#0067B3"
    )
    button.place(relx=0.8, y=150, anchor="center")
    
    for i in range(3):
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
        rectangle1.place(x=550, y=10)  # Posisi y disesuaikan agar terlihat dalam frame

        status_label = CTkLabel(
            rectangle1,
            text="BELUM DIAMBIL PEMILIK",
            font=("Poppins SemiBold", 10),
            text_color="#FFBB38"
        )
        # Posisi tetap relatif terhadap rectangle1
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
            text="Gedung F304",
            font=("Poppins Regular", 10),
            text_color="#000000"
        )
        location_label.place(x=230, y=50)

        # Main Item Name
        item_name_label = CTkLabel(
            lost_frame,
            text="Kunci Motor",
            font=("Poppins SemiBold", 14),
            text_color="#000000"
        )
        item_name_label.place(x=230, y=30)

        # Description
        description_label = CTkLabel(
            lost_frame,
            text="Ditemukan Pada Saat Peralihan sesi2\ndi Gedung F",
            font=("Poppins Regular", 10),
            text_color="#000000",
            justify="left"
        )
        description_label.place(x=230, y=70)

        # Item Image
        item_image_path = assets_path / "kunci.png"  # Replace with actual image path
        item_image = CTkImage(
            light_image=Image.open(item_image_path),
            size=(200, 80)
        )
        item_image_label = CTkLabel(
            lost_frame,
            image=item_image,
            text=""
        )
        item_image_label.place(x=10, y=40)

        report_button = CTkButton(
            lost_frame,
            text="Sampaikan Kepemilikan Barang",
            font=("Poppins SemiBold", 11),
            fg_color="#7650E1",
            text_color="#FFFFFF",
            width=215,
            height=30,
            corner_radius=5,
            command=lambda: print("Report button clicked")
        )
        report_button.place(x=450, y=100)