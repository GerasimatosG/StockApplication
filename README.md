# 📈 Stock App

A simple stock app that connects Python with PostgreSQL and creates API requests to interact with the database.

## 🌟 Features

- Connects to a PostgreSQL database
- Provides a basic interface for API requests to interact with stock data
- Supports CRUD operations

## 🛠️ Requirements

- Python 3.8+
- PostgreSQL 12+
- pgAdmin4
- Requests (or any HTTP library for API requests)

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/GerasimatosG/stock-app.git
    cd stock-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:
    - Ensure PostgreSQL is installed and running.
    - Open pgAdmin4 and create a new database:
      - Name: `stock_app_db`
    - Create necessary tables using SQL scripts or pgAdmin4 interface.

5. **Configure database connection**:
    - Update your database configuration in your Python script to connect to `stock_app_db`.

## 🎉 Usage

1. **Run your Python application**:
    ```bash
    python main.py
    ```

2. The app will perform API requests and interact with the PostgreSQL database.
