'''
Run club project
Author: @Carlos Raniel Ariate Arro

'''


import customtkinter as ctk
import sys
app = ctk.CTk()
app.geometry("500x500")
#Title section

# dataset
records= []

def showPage(page):
    page.tkraise()

def submitRecord():
    pass

def exit():
    sys.exit()
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
returnBtn = ctk.CTkButton(
    addPage,
    text="Return",
    command = lambda:showPage(mainPage)
)
returnBtn.grid(row=0,column=0,pady=30,padx=20)

addTitle = ctk.CTkLabel(
    addPage,
    text="Add new record"
)
addTitle.grid(row=0,column=1,pady=30,padx=20)
nameEntry = ctk.CTkEntry(
    addPage,
    placeholder_text= "Enter name "   
)
nameEntry.grid(row=1,column=1,pady=30,padx=20)
timeEntry = ctk.CTkEntry(
    addPage,
    placeholder_text="time in seconds"
)
timeEntry.grid(row=4,column=1,pady=30,padx=20)

submitbtn = ctk.CTkButton(
    addPage,
    text="Submit",
    command=submitRecord
)
submitbtn.grid(row=5,column=1,pady=30,padx=20)

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
    command = exit
)
exitBtn.pack(pady=20)

for page in (mainPage,addPage,viewRecords):
    page.grid(row=0,column=0,sticky="nsew")
mainPage.tkraise()
app.mainloop()