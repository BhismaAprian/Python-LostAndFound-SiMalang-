from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
import firebase_admin
from firebase_admin import credentials, storage, db
from io import BytesIO
import requests
import os
from tkinter import filedialog

def upload_image_to_firebase(image_path):
    bucket = storage.bucket()
    blob = bucket.blob(f"images/{os.path.basename(image_path)}")
    blob.upload_from_filename(image_path)
    blob.make_public()  
    return blob.public_url

def save_to_firebase(data):
    ref = db.reference("found")
    
    items = ref.get()
    if not items:
        next_item_id = 1
    else:
        next_item_id = len(items) + 1
    
    item_id = f"item_{next_item_id}"
    ref.child(item_id).set(data)

def submit_form(item_name, location, description, user_id, image_path):
    image_url = upload_image_to_firebase(image_path)

    data = {
        "description": description,
        "id": None,  
        "images": image_url,
        "is_found": False,
        "location": location,
        "name": item_name,
        "user_id": user_id
    }
    
    save_to_firebase(data)
    print(f"Item {item_name} telah disimpan ke Firebase.")

def upload_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

def relative_to_assets(path):
    return f"assets/{path}"

def render_form(parent_frame, user_id):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    title_label = CTkLabel(
        parent_frame,
        text="Form Pengajuan Penemuan",
        font=("Poppins", 36),
        text_color="#353E6C"
    )
    title_label.place(x=47, y=117)

    photo_label = CTkLabel(
        parent_frame,
        text="Foto Barang",
        font=("Poppins Regular", 13),
        text_color="#3C3C43"
    )
    photo_label.place(x=45, y=206)

    upload_button = CTkButton(
        parent_frame,
        text="Unggah Foto",
        font=("Poppins Regular", 12),
        command=lambda: print("Unggah Foto clicked"),
        fg_color="#0067B3",
        width=162,
        height=40
    )
    upload_button.place(x=155, y=197)

    item_name_label = CTkLabel(
        parent_frame,
        text="Nama Barang",
        font=("Poppins Regular", 13),
        text_color="#3C3C43"
    )
    item_name_label.place(x=45, y=272)

    item_name_entry = CTkEntry(
        parent_frame,
        placeholder_text="Masukkan nama barang",
        width=705,
        height=45,
        fg_color="white"
    )
    item_name_entry.place(x=60, y=294)

    location_label = CTkLabel(
        parent_frame,
        text="Lokasi Ditemukan",
        font=("Poppins Regular", 13),
        text_color="#3C3C43"
    )
    location_label.place(x=45, y=353)

    # Input Lokasi Ditemukan
    location_entry = CTkEntry(
        parent_frame,
        placeholder_text="Masukkan lokasi ditemukan",
        width=705,
        height=45,
        fg_color="white"
    )
    location_entry.place(x=61, y=375)

    # Label Deskripsi
    description_label = CTkLabel(
        parent_frame,
        text="Deskripsi",
        font=("Poppins Regular", 13),
        text_color="#3C3C43"
    )
    description_label.place(x=48, y=444)

    description_entry = CTkEntry(
        parent_frame,
        placeholder_text="Masukkan deskripsi",
        width=705,
        height=45,
        fg_color="white"
    )
    description_entry.place(x=62, y=467)

    submit_button = CTkButton(
        parent_frame,
        text="Submit",
        font=("Poppins SemiBold", 14),
        command=lambda: submit_form(item_name_entry.get(), location_entry.get(), description_entry.get(), user_id, upload_photo()),
        fg_color="#0067B3",
        width=94,
        height=40
    )
    submit_button.place(x=688, y=569)

if __name__ == "__main__":
    app = CTk()
    app.geometry("800x600")
    app.title("CustomTkinter Form")

    main_frame = CTkFrame(app, fg_color="#F5F5F5")
    main_frame.pack(fill="both", expand=True)

    render_form(main_frame)

    app.mainloop()
