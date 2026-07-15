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


#create container
container = ctk.CTkFrame(app)
container.pack(fill="both",expand=True)
container.grid_rowconfigure(0,weight=1)
container.grid_columnconfigure(0,weight=1)
#Main Page

mainPage = ctk.CTkFrame(container)

title = ctk.CTkLabel(
    mainPage,
    text = "Run club project"
)

newEntryBtn = ctk.CTkButton(
    mainPage,
    text = "Enter new record",
    command = lambda: showPage(addPage)
)

viewRecordsBtn = ctk.CTkButton(
    mainPage,
    text = " View records",
    command = lambda: showPage(viewRecords)
)
exitBtn = ctk.CTkButton(
    mainPage,
    text ="Exit",
)
addPage = ctk.CTkFrame(container)
addTitle = ctk.CTkLabel(
    addPage,
    text="Add new record"
)

viewRecords = ctk.CTkFrame(container)
viewRecordsTitle = ctk.CTkLabel(
    viewRecords,
    text="View Records"
)


#packing all home pages 
title.pack(pady=30)
newEntryBtn.pack(pady=20)
viewRecordsBtn.pack(pady=20)
exitBtn.pack(pady=20)


#packing all addPage
addTitle.pack(pady=30)

#packing all ViewRecords
viewRecordsTitle.pack(pady=30)

for page in (mainPage,addPage,viewRecords):
    page.grid(row=0,column=0,sticky="nsew")
mainPage.tkraise()
app.mainloop()