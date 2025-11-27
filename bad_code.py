import sqlite3
import os

# ОШИБКА 1: Хардкод секретов (Security)
AWS_SECRET_KEY = "AKIA1234567890" 

def get_user_info(user_id):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # ОШИБКА 2: SQL Injection (Security)
    # Использование f-string вместо параметризированного запроса
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    return cursor.fetchone()

def process_logs(log_path):
    try:
        # ОШИБКА 3: Performance
        # read() загружает весь файл в RAM. Если лог 10ГБ, сервер упадет.
        with open(log_path, 'r') as f:
            data = f.read()
            lines = data.split('\n')
            
        for line in lines:
            print(f"Processing {line}")
            
    # ОШИБКА 4: Robustness (Pokemon Exception Handling)
    # Мы не узнаем, если что-то пошло не так.
    except:
        pass
