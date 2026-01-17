# 🎓 Student Management System (SMS)

A comprehensive Student Management System built with Python, featuring two distinct versions that showcase the evolution from a basic CRUD application to a professional, feature-rich management suite.

---

## 📂 Project Structure

```text
Student-GUI-with-SQL/
├── 📁 Student-GUI-version1/      # Initial Version (Basic CRUD)
│   ├── gui_app.py                # Tkinter-based GUI
│   ├── school_db.sql             # MySQL Database Schema
│   └── .env                      # Database Configuration
├── 📁 Student-GUI-version2/      # Pro Version (Advanced Features)
│   ├── gui_app_v2.py             # CustomTkinter-based Pro UI
│   ├── database_helper.py        # Optimized DB Logic
│   ├── requirements.txt          # Project Dependencies
│   ├── Dockerfile                # Containerization Profile
│   └── .env.example              # Environment Template
├── .gitignore                    # Git Exclusion Rules
└── README.md                     # Project Documentation
```

---

## 🚀 Versions Overview

### 🔹 Version 1.0 (Basic)
*The foundation of the project.*
- **Interface**: Standard Python `Tkinter`.
- **Core Features**: Basic student registration and marks entry.
- **Goal**: Simple data persistence and database connectivity.
- **Usage**: Navigate to `Student-GUI-version1/` and run `python gui_app.py`.

### 🔹 Version 2.0 (Pro)
*A modern, high-performance management suite.*
- **Interface**: Sleek, responsive UI built with `CustomTkinter`.
- **Advanced Features**:
    - **Performance Analytics**: Visual charts using `Matplotlib`.
    - **Data Export**: One-click "Export to Excel" functionality.
    - **Modern UX**: Supports Dark/Light modes.
    - **Containerized**: Ready for deployment with `Docker`.
- **Goal**: Professional-grade administrative tool.
- **Usage**: See the detailed setup guide inside `Student-GUI-version2/`.

---

## 🛠 Tech Stack

- **Frontend**: Python (Tkinter, CustomTkinter)
- **Backend**: MySQL
- **Data Analysis**: Pandas, Matplotlib
- **DevOps**: Docker
- **Environment**: Python 3.10+

---

## 📝 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/toxicbishop/Student-GUI-With-SQL.git
   cd Student-GUI-With-SQL
   ```

2. **Choose a Version**:
   - For the **Basic** version, enter `Student-GUI-version1`.
   - For the **Pro** version, enter `Student-GUI-version2`.

3. **Configure Database**:
   Fill in your MySQL credentials in the `.env` file within the respective version folder.

4. **Install Dependencies**:
   ```bash
   pip install -r Student-GUI-version2/requirements.txt
   ```

5. **Execute**:
   ```bash
   python Student-GUI-version2/gui_app_v2.py
   ```

---

## 📄 License
This project is licensed under the MIT License.
