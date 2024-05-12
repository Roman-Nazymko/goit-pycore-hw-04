def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок по комі та витягаємо зарплату
                salary = line.strip().split(',')[1]
                # Додаємо зарплату до загальної суми
                total_salary += int(salary)
                num_developers += 1

        # Обчислюємо середню зарплату
        average_salary = total_salary / num_developers if num_developers > 0 else 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print("Виникла помилка при обробці файлу:", e)
        return None

# Приклад використання функції
total, average = total_salary("task_1//salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
