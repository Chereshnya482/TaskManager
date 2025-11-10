import src.data as data
import src.ui as ui
import src.logic as logic
import sys


def main():
    # 1. Загрузка данных
    tasks = data.load_tasks()

    # Главный цикл приложения
    while True:
        choice = ui.show_menu()

        # Переменная для отслеживания изменений (для автосохранения)
        data_changed = False

        if choice == '1':  # Добавить задачу
            task_data = ui.get_task_input()
            if task_data:
                logic.add_task(tasks, task_data)
                data_changed = True

        elif choice == '2':  # Показать список задач
            ui.display_tasks(tasks)

        elif choice == '3':  # Изменить статус
            task_id = ui.get_task_id("Введите ID задачи для изменения статуса: ")
            if task_id is not None:
                new_status = ui.get_new_status()
                if new_status:
                    if logic.change_status(tasks, task_id, new_status):
                        print(f"✅ Статус задачи ID:{task_id} изменен на '{new_status}'.")
                        data_changed = True
                    else:
                        print(f"❌ Задача с ID:{task_id} не найдена.")

        elif choice == '4':  # Редактировать задачу
            task_id = ui.get_task_id("Введите ID задачи для редактирования: ")
            if task_id is not None:
                print("\n--- Редактирование задачи ---")
                new_data = ui.get_task_input()
                if new_data:
                    if logic.edit_task(tasks, task_id, new_data['title'], new_data['description']):
                        print(f"✅ Задача ID:{task_id} успешно отредактирована.")
                        data_changed = True
                    else:
                        print(f"❌ Задача с ID:{task_id} не найдена.")

        elif choice == '5':  # Удалить задачу (одиночное)
            task_id = ui.get_task_id("Введите ID задачи для удаления: ")
            if task_id is not None:
                if logic.delete_task(tasks, task_id):
                    print(f"🗑️ Задача ID:{task_id} успешно удалена.")
                    data_changed = True
                else:
                    print(f"❌ Задача с ID:{task_id} не найдена.")

        elif choice == '6':  # Массовое удаление (завершенные)
            deleted_count = logic.mass_delete_completed(tasks)
            if deleted_count > 0:
                print(f"🗑️ Удалено {deleted_count} завершенных задач.")
                data_changed = True
            else:
                print("ℹ️ Завершенных задач для удаления не найдено.")

        elif choice == 'q':
            break

        else:
            print("❌ Неверный выбор. Пожалуйста, повторите ввод.")

        # Автосохранение при изменениях
        if data_changed:
            data.save_tasks(tasks)

    # Финальное автосохранение при выходе
    print("\n👋 Сохранение и выход. Спасибо за использование TaskManager!")
    data.save_tasks(tasks)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Обработка Ctrl+C
        print("\n\nПрограмма прервана пользователем.")
        # Принудительное сохранение при выходе по прерыванию
        data.save_tasks(data.load_tasks())
        sys.exit(0)