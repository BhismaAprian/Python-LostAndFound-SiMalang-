from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton
from PIL import Image

def render_lost_content(parent_frame):
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
        command=lambda: print("Ajukan Kehilangan clicked"),
        fg_color="#FFBB38"
    )
    button.place(relx=0.5, y=150, anchor="center")
    
    item_frame = CTkFrame(
        parent_frame,
        width=1200,
        height=800,
        fg_color="#FFFFFF",
        corner_radius=10
    )
    item_frame.place(relx=0.5, rely=0.5, anchor="center")

    item_label = CTkLabel(
        item_frame,
        text="Nama Barang: Kunci Motor\nLokasi: Gedung F304",
        font=("Poppins Regular", 14),
        justify="left"
    )
    item_label.pack(pady=10, padx=10)
