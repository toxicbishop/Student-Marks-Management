# 🎓 Student Marks Management System

A robust **Console User Interface (CUI)** application built with Python and MySQL to manage student academic records. This project demonstrates database normalization, Python-SQL connectivity, and efficient data entry workflows.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?style=flat&logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview

This application serves as a data entry tool for educational institutions. It allows administrators to:
1.  Register new students or identify existing ones by Roll Number.
2.  Input marks for a predefined curriculum (Science, Social, Maths, English, Hindi, Kannada).
3.  Automatically generate unique transaction IDs (UUID) for every record.
4.  Store data securely in a normalized relational database.

## ⚙️ Features

* **Remote Database Connection:** Capable of connecting to remote MySQL servers on custom ports.
* **Data Normalization:** Uses three separate tables (`STUDENTS`, `SUBJECTS`, `MARKS`) to reduce redundancy.
* **Smart Error Handling:** * Detects if a student already exists and automatically switches to "Update" mode.
    * Validates integer inputs to prevent crashes.
    * Handles network timeouts gracefully.
* **Secure Configuration:** Uses dictionary unpacking (`**kwargs`) for clean and secure database connection management.

## 🗄️ Database Schema

The project uses a Relational Database design:

| Table | Primary Key | Description |
| :--- | :--- | :--- |
| **STUDENTS** | `ROLL_NO` | Stores student Name and Roll Number. |
| **SUBJECTS** | `SUBJ_ID` | Stores Subject IDs (101-106) and Names. |
| **MARKS** | `ID` (UUID) | Links Student, Subject, and Marks together. |

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Database:** MySQL (Remote or Local)
* **Libraries:** * `pymysql` (For database connectivity)
    * `uuid` (For generating unique IDs)
    * `sys` (For standard input handling)

## 🚀 Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/student-marks-system.git](https://github.com/yourusername/student-marks-system.git)
    cd student-marks-system
    ```

2.  **Install dependencies:**
    This project requires the `pymysql` driver.
    ```bash
    pip install pymysql
    ```

3.  **Database Setup:**
    Execute the following SQL commands in your MySQL Workbench or DBeaver to create the required tables:
    ```sql
    CREATE TABLE IF NOT EXISTS STUDENTS (
        ROLL_NO INT PRIMARY KEY,
        NAME VARCHAR(50)
    );
    
    CREATE TABLE IF NOT EXISTS SUBJECTS (
        SUBJ_ID INT PRIMARY KEY,
        SUBJ_NAME VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS MARKS (
        ID CHAR(36) PRIMARY KEY, 
        ROLL_NO INT,
        SUBJ_ID INT,
        MARKS INT,
        FOREIGN KEY (ROLL_NO) REFERENCES STUDENTS(ROLL_NO),
        FOREIGN KEY (SUBJ_ID) REFERENCES SUBJECTS(SUBJ_ID)
    );
    
    -- Pre-populate subjects
    INSERT IGNORE INTO SUBJECTS VALUES (101, 'Science'), (102, 'Social'), (103, 'Maths'), (104, 'English'), (105, 'Hindi'), (106, 'Kannada');
    ```

## 📝 Configuration

Open the `main.py` file and update the `DB_CONFIG` dictionary with your database credentials. 

> **⚠️ IMPORTANT:** Never commit your real passwords to GitHub! Use environment variables or a separate config file in a real-world scenario.

```python
DB_CONFIG = {
    'host': 'your-server-ip.com',  # e.g., localhost or a remote IP
    'port': 3306,                  # Default is 3306, change if needed
    'user': 'your-username',
    'password': 'your-password',
    'database': 'school_db',
    'cursorclass': pymysql.cursors.DictCursor
}
