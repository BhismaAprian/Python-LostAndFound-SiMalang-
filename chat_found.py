from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkSwitch
from PIL import Image
from io import BytesIO
from firebase_admin import db
import requests
from datetime import datetime
import tkinter as tk  # Menggunakan tkinter untuk IntVar dan lainnya

def start_chat(parent_frame, user_id, item_id):
    chat_ref = db.reference(f'chats/found/{item_id}') 
    users_ref = db.reference('users')  
    item_ref = db.reference(f'found/{item_id}')  

    def send_message():
        timestamp = datetime.utcnow().isoformat()  
        message_text = chat_entry.get()
        
        if message_text.strip():
            user_data = users_ref.child(str(user_id)).get()  
            if user_data and 'name' in user_data:
                sender_name = user_data['name']
            else:
                sender_name = 'Unknown'  

            message_data = {
                'sender': sender_name,  
                'message': message_text,
                'timestamp': timestamp
            }

            chat_ref.push(message_data)
            chat_entry.delete(0, 'end')
            load_messages()  

    def load_messages():
        for widget in chat_frame.winfo_children():
            widget.destroy()

        loaded_messages = set()  

        def on_message_event(event):
            messages = chat_ref.order_by_child('timestamp').get()
            if messages:
                for key, msg in messages.items():
                    if key not in loaded_messages:  
                        sender = msg.get('sender', 'Unknown')
                        message = msg.get('message', '')
                        timestamp = msg.get('timestamp', '')

                        message_label = CTkLabel(
                            chat_frame,
                            text=f"{sender}: {message}",
                            font=("Poppins Regular", 10),
                            text_color="#000000",
                            wraplength=400,
                            justify="left"
                        )
                        message_label.pack(anchor="w", pady=2, padx=5)

                        loaded_messages.add(key)  

        chat_ref.listen(on_message_event)

    def update_is_found():
        item_ref.update({'is_found': is_found_var.get()})

    item_data = item_ref.get()
    initial_is_found = item_data.get('is_found', False)

    for widget in parent_frame.winfo_children():
        widget.destroy()

    CTkLabel(
        parent_frame,
        text="Chat Room",
        font=("Poppins SemiBold", 20),
        text_color="#353E6C"
    ).pack(pady=10)

    chat_frame = CTkFrame(parent_frame, width=400, height=400, fg_color="#F5F5F5")
    chat_frame.pack(fill="both", expand=True, padx=20, pady=10)

    chat_entry = CTkEntry(parent_frame, placeholder_text="Type a message", width=300)
    chat_entry.pack(side="left", padx=10, pady=10)

    send_button = CTkButton(
        parent_frame,
        text="Send",
        command=send_message,
        fg_color="#0067B3"
    )
    send_button.pack(side="left", pady=10)

    is_found_var = tk.BooleanVar(value=initial_is_found)  
    toggle_button = CTkSwitch(
        parent_frame,
        text="Sudah Di Ambil Pemilik?",
        variable=is_found_var,  
        onvalue=True, 
        offvalue=False, 
        command=update_is_found 
    )
    toggle_button.pack(pady=20)

    load_messages()
