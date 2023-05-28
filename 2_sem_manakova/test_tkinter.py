import tkinter as tk
from tkinter import messagebox
from dop_parser import choose_catalog
from parser_main import get_content

# Функция для обработки нажатия кнопки
def parse_data():
    # Получаем значения из текстовых полей
    count = int(count_entry.get())
    low = int(low_entry.get())
    top = int(top_entry.get())

    try:
        shard, query = choose_catalog(catalog_var.get())
        data = get_content(shard, query, count, low, top)
        # Отображаем результаты парсинга в текстовом поле
        result_text.delete('1.0', tk.END)  # Очищаем текстовое поле
        for item in data:
            result_text.insert(tk.END, f"{item}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"{e} Каталог не найден")

# Создаем графический интерфейс
window = tk.Tk()
window.title("Парсер данных")
window.geometry("400x300")

# Создаем метку и текстовое поле для выбора каталога
catalog_label = tk.Label(window, text="Выберите каталог:")
catalog_label.pack()

catalog_var = tk.StringVar()
catalog_dropdown = tk.OptionMenu(window, catalog_var, "Здоровье", "Брюки", "Красота")
catalog_dropdown.pack()

# Создаем метки и текстовые поля для ввода параметров
count_label = tk.Label(window, text="Количество страниц (до 100):")
count_label.pack()

count_entry = tk.Entry(window)
count_entry.pack()

low_label = tk.Label(window, text="Нижняя цена:")
low_label.pack()

low_entry = tk.Entry(window)
low_entry.pack()

top_label = tk.Label(window, text="Верхняя цена:")
top_label.pack()

top_entry = tk.Entry(window)
top_entry.pack()

# Создаем кнопку для запуска парсинга
parse_button = tk.Button(window, text="Начать парсинг", command=parse_data)
parse_button.pack()

# Создаем текстовое поле для отображения результатов
result_text = tk.Text(window)
result_text.pack()

window.mainloop()
