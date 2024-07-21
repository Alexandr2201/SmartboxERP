import os
import sys

# Определяем путь
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))

# Добавляем путь в sys.path
sys.path.insert(0, path_to_add)

# Выводим путь для проверки
print("Path added to sys.path:", path_to_add)

# Проверяем наличие пути в sys.path
print("Current sys.path:")
for path in sys.path:
    print(path)