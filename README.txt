# RPG Session Tracker (CLI)

## Simple command-line application to manage RPG players and characters using Python and MySQL.

---

## Features
- Add, update, delete and display players
- Add, update, delete and display characters
- Link characters to players
- Basic input validation
- Add, update, delete and display sessions
- Add, update, delete and display events
- Link multiple events to one session and display all for this one session
---

## Tech Stack
Python
MySQL
mysql-connector-python

---

## Setup
### Clone the repository:
git clone https://github.com/sszJakub/rpg-session-tracker.git
cd rpg-session-tracker

### Install dependencies:
pip install -r requirements.txt

### Create a credentials.py file:
    "my_host": "localhost",
    "my_user": "your_user",
    "my_password": "your_password",
    "my_database": "rpg_db"

### Create database and tables in MySQL.

---

## Run the app:
python main.py
Example:
Add a player

Assign characters to players
Manage data via CLI menu

---

## Future Improvements
- Better UI
- Search functionality