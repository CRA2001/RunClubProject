---

# 🏃 Running Club Management System

A desktop application built with **Python** and **CustomTkinter** that transforms a traditional **Cambridge IGCSE Computer Science (0478) Paper 2 15-mark programming question** into a modern graphical application.

Instead of interacting through the console, this project provides a clean GUI for entering competitors, validating results, sorting performance, awarding prizes, and generating certificates.

---

## 📖 About the Project

This project was created as both a programming exercise and a way to explore desktop application development using **CustomTkinter**.

The original examination question required students to write a console-based solution using arrays. This application recreates the same logic while adding a modern user interface and improved usability.

The project demonstrates how examination algorithms can be transformed into real software.

---

## ✨ Features

* Add running club members
* Enter running times with double-entry verification
* Automatically validate matching inputs
* Sort members by their running times
* Display the top three runners

  * 🥇 First Place
  * 🥈 Second Place
  * 🥉 Third Place
* Automatically determine certificate recipients (under 240 seconds)
* Display the total number of certificates to print
* Modern desktop interface using CustomTkinter

---

## 🧠 Concepts Demonstrated

This project makes use of many core IGCSE Computer Science concepts, including:

* One-dimensional arrays (lists)
* Data validation
* Sequential processing
* Bubble sort (or another sorting algorithm)
* Parallel arrays
* Selection (`if`)
* Iteration (`for` / `while`)
* Functions
* GUI programming
* Event-driven programming

---

## 🛠 Technologies Used

* Python 3
* CustomTkinter
* Tkinter
* Git
* GitHub

---

## 📂 Project Structure

```text
RunningClubApp/
│
├── assets/              # Images and icons
├── src/                 # Application source code
│   ├── main.py
│   ├── ui.py
│   ├── logic.py
│   └── ...
│
├── README.md
└── requirements.txt
```

*(Project structure may change as development continues.)*

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/running-club-management.git
```

Navigate into the project:

```bash
cd running-club-management
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 🎯 Learning Objectives

This project aims to:

* Practice Python programming
* Learn desktop GUI development
* Understand event-driven programming
* Improve software design skills
* Apply examination algorithms to real-world applications
* Gain experience using Git and GitHub

---

## 📚 Original Examination Requirements

The original problem required the program to:

* Input each member's running time twice and verify both entries match
* Store names and times using parallel arrays
* Sort members by their running times
* Award prizes to the fastest three runners
* Store members with times below **240 seconds** for certificate printing
* Output the number of certificates to be printed

This application satisfies these requirements while presenting them through a graphical user interface.

---

## 🔮 Future Improvements

Possible future enhancements include:

* Save and load member data
* Export certificate lists to CSV
* Search members
* Edit existing records
* Statistics dashboard
* Graphs of running times
* Dark and light themes
* Database integration (SQLite)

---

## 📜 License

This project is intended for educational purposes and personal learning.

The original programming scenario is inspired by a Cambridge IGCSE Computer Science examination question. The implementation and graphical interface are original.

---