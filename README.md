# VelvetKey-Password-Manager-using-Flask
VelvetKey is a Flask-based web application that allows users to securely store and manage their passwords. With an intuitive interface and robust backend, VelvetKey makes password management simple and safe.

![VelvetKey Logo](static/images/VelvetKey4.gif)

## 🌟 Features

- **User-Friendly Interface**: Easy-to-use web interface for managing your passwords.
- **CRUD Operations**: Create, Read, Update, and Delete password entries with ease.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Nik7125/VelvetKey-Password-Manager-using-Flask.git
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
velvetkey/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── VelvetKey4.gif
│
└── templates/
    ├── base.html
    ├── index.html
    ├── create.html
    └── update.html
```

## 🛠 Technology Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (easily upgradable to other SQL databases)

Project Link: https://github.com/Nik7125/VelvetKey-Password-Manager-using-Flask

---

Made with ❤️ and ☕
