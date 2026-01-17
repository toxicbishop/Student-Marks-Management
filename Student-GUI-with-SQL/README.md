# 🎓 Student Management System Pro (SMS PRO)

A modern, high-performance Student Management System built with Python, CustomTkinter, and MySQL. This application provides a comprehensive suite for managing student records, performance analytics, and data export.

## ✨ Features

- **Modern UI**: Sleek, responsive interface built with `CustomTkinter`.
- **Student Records**: Easily add, view, search, and delete student data.
- **Mark Management**: Dedicated section for subject-wise marks entry.
- **Performance Analytics**: Visual representation of class performance using `Matplotlib`.
- **Data Export**: Export student records to Excel with a single click.
- **Dark/Light Mode**: Customizable appearance to suit your preference.
- **Database Backend**: Secure data persistence using MySQL.
- **Dockerized**: Containerized for easy deployment and consistent environments.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MySQL Server
- X Server (if running via Docker on Windows/Mac, e.g., VcXsrv)

### Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/toxicbishop/Student-GUI-With-SQL.git
   cd Student-GUI-With-SQL
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory based on `.env.example`:
   ```env
   DB_HOST=your_host
   DB_USER=your_user
   DB_PASS=your_password
   DB_NAME=your_db_name
   DB_PORT=3306
   ```

5. **Run the application**:
   ```bash
   python gui_app_v2.py
   ```

### Running with Docker

1. **Build the image**:
   ```bash
   docker build -t sms-pro .
   ```

2. **Run the container**:
   Ensure an X Server is running on your host machine.
   ```bash
   docker run -it --rm -e DISPLAY=host.docker.internal:0.0 sms-pro
   ```

## 🛠 Tech Stack

- **Frontend**: CustomTkinter (Python)
- **Backend**: MySQL
- **Data Analysis**: Pandas, Matplotlib
- **Containerization**: Docker

## 📝 License

This project is licensed under the MIT License.
