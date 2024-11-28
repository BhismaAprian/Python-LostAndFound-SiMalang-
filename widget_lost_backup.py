from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image

def render_lost_content(parent_frame, assets_path):
    # Frame utama
    lost_frame = CTkFrame(
        parent_frame,
        width=685,
        height=135,
        fg_color="#FFFFFF",
        corner_radius=10
    )
    lost_frame.pack(pady=10, padx=10)

    # Rectangle-like box 1
    rectangle1 = CTkFrame(
        lost_frame,
        width=107,
        height=13,
        fg_color="#FFF5D9",
        corner_radius=0
    )
    rectangle1.place(x=380, y=17)  # Adjusted position

    status_label = CTkLabel(
        rectangle1,
        text="BELUM DITEMUKAN",
        font=("Poppins SemiBold", 7),
        text_color="#FFBB38"
    )
    status_label.place(relx=0.5, rely=0.5, anchor="center")

    # Rectangle-like box 2 (vertical line)
    rectangle2 = CTkFrame(
        lost_frame,
        width=1,
        height=85,
        fg_color="#DEDEDE",
        corner_radius=0
    )
    rectangle2.place(x=220, y=40)  # Adjusted position

    # Text: Gedung F304
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
        text="Hilang Pada Saat Peralihan sesi2\ndi Gedung F",
        font=("Poppins Regular", 10),
        text_color="#000000",
        justify="left"
    )
    description_label.place(x=230, y=70)

    # Item Image
    item_image_path = assets_path / "image_1.png"  # Replace with actual image path
    item_image = CTkImage(
        light_image=Image.open(item_image_path),
        size=(50, 50)
    )
    item_image_label = CTkLabel(
        lost_frame,
        image=item_image,
        text=""
    )
    item_image_label.place(x=10, y=40)

    # "Sampaikan Penemuan Barang" Button
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
    report_button.place(x=400, y=100)