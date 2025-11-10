import time


def get_next_id(tasks):
    if not tasks:
        return 1
    # Находим максимальный ID и увеличиваем его на 1
    return max(task.get('id', 0) for task in tasks) + 1


def add_task(tasks, task_data):
    new_id = get_next_id(tasks)

    # Полная структура задачи
    new_task = {
        'id': new_id,
        'title': task_data['title'],
        'description': task_data.get('description', ''),
        'status': 'новая',  # 'новая', 'в работе', 'завершена'
        'created_at': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    print(f"✅ Задача ID:{new_id} '{new_task['title']}' добавлена.")
    return True


def change_status(tasks, task_id, new_status):
    for task in tasks:
        if task['id'] == task_id:
            valid_statuses = ['новая', 'в работе', 'завершена']
            if new_status in valid_statuses:
                task['status'] = new_status
                return True
            else:
                print(f"❌ Неверный статус: '{new_status}'. Доступны: {', '.join(valid_statuses)}")
                return False
    return False  # ID не найден


def edit_task(tasks, task_id, new_title, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = new_title
            task['description'] = new_description
            return True
    return False


def delete_task(tasks, task_id):
    initial_len = len(tasks)
    # Используем list comprehension для удаления
    tasks[:] = [task for task in tasks if task['id'] != task_id]

    return len(tasks) < initial_len


def mass_delete_completed(tasks):
    initial_len = len(tasks)
    # Фильтруем список, оставляя только незавершенные задачи
    tasks[:] = [task for task in tasks if task['status'] != 'завершена']
    deleted_count = initial_len - len(tasks)
    return deleted_count