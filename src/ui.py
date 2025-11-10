import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    clear_screen()
    print("=" * 30)
    print("✨ TaskManager v1.0")
    print("=" * 30)
    print("1. Добавить задачу")
    print("2. Показать список задач")
    print("3. Изменить статус задачи")
    print("4. Редактировать задачу")
    print("5. Удалить задачу")
    print("6. Удалить все завершенные задачи (Массовое)")
    print("q. Выход")
    print("-" * 30)

    choice = input("Выберите действие: ").strip().lower()
    return choice


def get_task_input():
    print("\n--- Добавление новой задачи ---")
    title = input("Название: ").strip()
    description = input("Описание (можно пропустить): ").strip()

    if not title:
        print("❌ Название не может быть пустым.")
        return None

    return {'title': title, 'description': description}


def display_tasks(tasks):
    clear_screen()
    if not tasks:
        print("ℹ️ Список задач пуст.")
        input("Нажмите Enter для продолжения...")
        return

    print("=" * 70)
    print(f"| {'ID':<3} | {'Статус':<10} | {'Название':<25} | {'Создана':<19} |")
    print("=" * 70)

    for task in tasks:
        status = task['status']
        # Выделение статуса цветом (если поддерживается терминалом)
        color_map = {'новая': '\033[94m', 'в работе': '\033[93m', 'завершена': '\033[92m'}
        status_colored = f"{color_map.get(status, '')}{status:<10}\033[0m"

        print(f"| {task['id']:<3} | {status_colored} | {task['title'][:25]:<25} | {task['created_at'][5:16]:<19} |")

    print("=" * 70)
    print("\n")
    input("Нажмите Enter для продолжения...")


def get_task_id(prompt="Введите ID задачи: "):
    while True:
        try:
            task_id = input(prompt).strip()
            if not task_id:
                return None
            return int(task_id)
        except ValueError:
            print("❌ Ошибка: Введите целое числовой ID.")
            continue


def get_new_status():
    print("\nДоступные статусы: 1-новая, 2-в работе, 3-завершена")

    while True:
        status_choice = input("Выберите новый статус (1/2/3): ").strip()
        if status_choice == '1':
            return 'новая'
        elif status_choice == '2':
            return 'в работе'
        elif status_choice == '3':
            return 'завершена'
        elif not status_choice:
            return None
        else:
            print("❌ Неверный ввод. Пожалуйста, введите 1, 2 или 3.")