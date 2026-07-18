'''
Run club project
Author: @Carlos Raniel Ariate Arro

'''


import customtkinter as ctk
app = ctk.CTk()
app.geometry("500x500")
#Title section

# dataset
records= []

def showPage(page):
    page.tkraise()


#--------------------------create container--------------------------
container = ctk.CTkFrame(app)
container.pack(fill="both",expand=True)
container.grid_rowconfigure(0,weight=1)
container.grid_columnconfigure(0,weight=1)
#--------------------------Main Page--------------------------
mainPage = ctk.CTkFrame(container)
title = ctk.CTkLabel(
    mainPage,
    text = "Run club project"
)
title.pack(pady=30)

#--------------------------newEntryBtn--------------------------
newEntryBtn = ctk.CTkButton(
    mainPage,
    text = "Enter new record",
    command = lambda: showPage(addPage)
)
newEntryBtn.pack(pady=20)
addPage = ctk.CTkFrame(container)
addTitle = ctk.CTkLabel(
    addPage,
    text="Add new record"
)
addTitle.pack(pady=30)
#--------------------------View Records--------------------------
viewRecordsBtn = ctk.CTkButton(
    mainPage,
    text = " View records",
    command = lambda: showPage(viewRecords)
)
viewRecordsBtn.pack(pady=20)
viewRecords = ctk.CTkFrame(container)
viewRecordsTitle = ctk.CTkLabel(
    viewRecords,
    text="View Records"
)
viewRecordsTitle.pack(pady=30)

#--------------------------Exit button--------------------------
exitBtn = ctk.CTkButton(
    mainPage,
    text ="Exit",
)
exitBtn.pack(pady=20)

for page in (mainPage,addPage,viewRecords):
    page.grid(row=0,column=0,sticky="nsew")
mainPage.tkraise()
app.mainloop()