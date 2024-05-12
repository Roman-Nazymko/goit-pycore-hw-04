import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для автоматичного скидання кольорів після кожного виводу
init(autoreset=True)

def display_directory_structure(directory_path, indent=0):
    # Перетворення шляху до директорії у об'єкт типу Path
    directory = Path(directory_path)

    # Перевірка, чи існує вказаний шлях та чи є він директорією
    if not directory.is_dir():
        # Виведення повідомлення про помилку червоним кольором, якщо шлях не існує або не є директорією
        print(Fore.RED + f"Директорія не існує або не є директорією: {directory_path}")
        return
    
    # Ітерація по елементам (файлам та директоріям) у вказаній директорії
    for item in directory.iterdir():
        if item.is_dir():  # Якщо елемент є директорією
            # Виведення назви директорії синім кольором та іконкою
            print(" " * (indent + 2) + Fore.BLUE + f"📂 {item.name}/")
            # Рекурсивний виклик функції display_directory_structure для відображення вмісту піддиректорії
            display_directory_structure(item, indent + 4)
        elif item.is_file():  # Якщо елемент є файлом
            # Виведення назви файлу зеленим кольором та іконкою
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")

if __name__ == "__main__":
    # Перевірка наявності коректної кількості аргументів командного рядка
    if len(sys.argv) != 2:
        # Виведення повідомлення про помилку червоним кольором, якщо кількість аргументів некоректна
        print(Fore.RED + "Потрібно вказати лише один аргумент - шлях до директорії.")
        sys.exit(1)
    
    # Отримання шляху до директорії з аргументів командного рядка
    directory_path = sys.argv[1]
    
    # Виклик функції display_directory_structure з вказаним шляхом до директорії
    display_directory_structure(directory_path)
