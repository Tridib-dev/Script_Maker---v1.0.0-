# Message Log — Python CLI Messaging System

A clean, minimal, and well-structured **command-line messaging application** built with Python. The system enables two users to exchange messages interactively, logs all messages with timestamps, and persists them to a file for later review.

This repository is intentionally focused on **code clarity, explicit control flow, and foundational software engineering discipline** rather than feature bloat.

---

## 🚀 Features

* Two-user interactive CLI messaging
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
└── README.md
```

---

## 🛠 Technologies Used

* **Language:** Python 3
* **Standard Libraries:**

  * `datetime` – timestamp generation
  * `os` – reliable file-path handling

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
2. Prompts two users to enter their names
3. Users send messages interactively via the terminal
4. Each message is validated, timestamped, and written to disk
5. At the end of the session, users may:

   * Display all logged messages
   * Clear the message history

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

* Supports only two users
* Uses plain-text storage
* Designed for single-session execution

These limitations are intentional and documented.

---

## 🔮 Future Improvements

* Multi-user support
* Encrypted message storage
* Message search and filtering
* GUI or web-based interface

---

## 📜 License

This project is open-source and intended for educational and learning purposes.
