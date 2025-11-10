import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            # Возвращает список словарей
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        # Если файл поврежден или пуст
        print("⚠️ Ошибка при чтении tasks.json. Начинаем с пустого списка.")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
    except IOError:
        print("❌ Ошибка при записи в tasks.json. Данные не сохранены.")