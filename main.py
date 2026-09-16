# ————— 🗂️ Органайзер файлов
# 0. Принимать путь рабочей папки через sys.argv[1]
# 1. Получить дату/расширение/размер подпапок
# 2. Дать возможность выводить список подпапок
# 3. Дать возможность отфильтровывать вывод подпапок по 3-м опциям: дата/расширение/размер

import os

path = 'My_Files/LA/log_analysis.py'
size_bytes = os.path.getsize(path)
size_KB = size_bytes / 1024
print(size_KB)
















# scan_folder_name = os.listdir(os.path.join('My_Files', 'TTT'))
# scan_folder_name = os.path.split('My_Files/TTT/README.md')
# scan_folder_name = os.path.basename('My_Files/TTT/tic_tac_toe.py')
# scan_folder_name = os.path.abspath('My_Files/TTT') # Преобразует относительный путь, в полный
# scan_folder_name = os.path.exists('My_Files/TTT') # Проверяет существует ли папка или файл указанные в пути
# scan_folder_name = os.path.isfile('My_Files/TTT') # Проверяет является ли путь файлом
# scan_folder_name = os.path.isdir('My_Files/TTT/tic_tac_toe.py') # Проверяется является ли путь директорией
# scan_folder_name = os.path.splitext('My_Files/LA/log_analysis.py')
# scan_folder_name = pathlib.Path('')
# files_in_folder = os.listdir(scan_folder_name)
# file_change_name = os.rename(input('Путь к исходному файлу: '), input('Новый путь/имя: '))

# print(os.path.join('MyFiles', 'TTT'))