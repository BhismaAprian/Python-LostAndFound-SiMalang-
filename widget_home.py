from pathlib import Path
import customtkinter as ctk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Tubes\widgetHome\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def render_home_content(parent_frame):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    canvas = ctk.CTkCanvas(
        parent_frame,
        bg="#F1F1F1",
        height=1024,
        width=837,
        bd=0,
        highlightthickness=0
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        39.0,
        134.0,
        827.0,
        367.0,
        fill="#0067B3",
        outline=""
    )

    image_image_1 = ctk.CTkImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(
        595.0,
        256.00000671037014,
        image=image_image_1
    )

    image_image_2 = ctk.CTkImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(
        715.0,
        240.0,
        image=image_image_2
    )

    canvas.create_text(
        67.0,
        147.0,
        anchor="nw",
        text="September 4,  2023",
        fill="#FFFFFF",
        font=("Poppins Regular", 16)
    )

    canvas.create_text(
        67.0,
        221.0,
        anchor="nw",
        text="Aplikasi SiMALANG memudahkan mahasiswa dan staf ITK dalam melaporkan atau mencari barang hilang dan ditemukan. Pengguna dapat mengunggah data barang serta melihat daftar barang yang terdaftar di sistem.",
        fill="#FFFFFF",
        font=("Poppins Regular", 14)
    )

    canvas.create_text(
        67.0,
        171.0,
        anchor="nw",
        text="Selamat Datang, 11241010",
        fill="#FFFFFF",
        font=("Poppins SemiBold", 32)
    )
