# Message Log — Python CLI Messaging System

A clean, minimal, and well-structured **command-line messaging application** built with Python. The system enables multiple users to exchange messages interactively, logs all messages with timestamps, and persists them to a txt and organised json file for later review.

This repository is intentionally focused on **code clarity, explicit control flow, and foundational software engineering discipline** rather than feature bloat.

---

## 🚀 Features

* Multi-character interactive CLI messaging
* Automatic timestamping of each message
* Persistent message storage in a text file
* Option to view complete conversation history
* Option to clear/reset all stored messages
* Modular and readable code structure

---

## 🧱 Project Structure

```
.
├── Script_maker.py   # Program entry point and CLI workflow
├── functions.py      # File utilities and Message abstraction
├── messages.txt      # Message log (auto-created at runtime)
├── README.md         # Detailed README
├── messages.json     # smart and organized script in json format  
├── Liscence          # MIT liscence
└── decoration.py     # two functions to decorate the output of the programme

```

---

## 🛠 Technologies Used

* **Language:** Python 3
* **Standard Libraries:**

  * `datetime` – timestamp generation
  * `os` – reliable file-path handling
  * `shutil` – designing and user friendly
  * `json` – reliable and reusable file-path 
No external dependencies are required.

---

## ▶️ How to Run

### Prerequisites

* Python 3.8 or higher

### Execution

```bash
python Script_maker.py
```

---

## 🔍 Program Workflow

1. Initializes or resets the message log file
2. Prompts as many  users wanted  to enter their names
3. Users send messages interactively via the terminal
4. Each message is validated, timestamped, and written to disk
5. At the end of the session, users may:

   * Display all logged messages
   * Clear the message history
   * organised json file of the script
   * userfriendly txt file for a clean script

---

## 🧠 Engineering Concepts Demonstrated

* Object-Oriented Programming (OOP)
* File handling and persistence
* Modular code organization
* Explicit loop control and state management
* Input validation and CLI interaction

---

## ⚖️ Design Philosophy

* **Explicit over implicit:** No hidden control flow
* **Readable over clever:** Prioritizes maintainability
* **Minimal but complete:** Focuses on correctness and structure

---

## 🚧 Limitations

* currently dont support an interractive UI

These limitations are intentional and documented.

---

## 🔮 Future Improvements

* Message search and filtering
* GUI or web-based interface

---

## 📜 License

This project is open-source and intended for educational and learning purposes.
