'''
Run club project
Author: @Carlos Raniel Ariate Arro

'''


import customtkinter as ctk
app = ctk.CTk()
app.geometry("500x500")
#Title section
title = ctk.CTkLabel(
    app,
    text = "Run club project"
)

newEntryBtn = ctk.CTkButton(
    app,
    text = "Enter new record"
)

viewRecordsBtn = ctk.CTkButton(
    app,
    text = " View records"
)
exitBtn = ctk.CTkButton(
    app,
    text ="Exit"
)
title.pack(pady=30)
newEntryBtn.pack(pady=20)
viewRecordsBtn.pack(pady=20)
exitBtn.pack(pady=20)
app.mainloop()