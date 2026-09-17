# ————— 🗂️ Органайзер файлов
# ✅ Принимать путь рабочей папки через sys.argv[1]
# o 1. Получить дату/расширение/размер подпапок
# ✅ Дать возможность выводить список подпапок
# o 3. Дать возможность отфильтровывать вывод подпапок по 3-м опциям: дата/расширение/размер
# 	✅ По расширению
# 	o По размеру
# 	o По дате

import os
import sys
from time import sleep
from time import ctime

print('\n—————————— 🗂️ Органайзер файлов\n')

path = sys.argv[1]
text_ext = ['.txt', '.py', '.log', '.docx', '.doc', '.pdf', '.html']
dirs = enumerate(os.listdir(path))

def default_sort(path):
	print(f'Вы выбрали фильтрацию по типу из {path}')
	sleep(0.5)
	print('Ожидайте...')

	dirs = sorted(os.listdir(path), key=lambda dir: os.path.splitext(dir)[-1])

	for index, dir in enumerate(dirs):
		sleep(1)
		print(f"{index + 1}. {dir}")

def dry_run(path):
	print(f'Вы выбрали простой вывод файлов из {path}')
	sleep(0.5)
	print('Ожидайте...')

	for index, dir in dirs:
		# ext = os.path.splitext(dir)[-1]
		sleep(1)
		print(f"{index + 1}. {dir}")

		# if ext in text_ext:
		# 	print(f'Type: {ext}')
		# else:
		# 	print()

def by_date(unsorted_dirs, path):
	print(f'Вы выбрали фильтрацию по дате из {path}')
	sleep(0.5)
	print('Ожидайте...')

	def sum_hours(dir):
		time = ctime(os.path.getmtime(dir)).split()
		print(time)
		input("...")

		months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
				  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
				]

		hours_year = ((time[4] * 365) * 24) # hours
		hours_month = ((months.index(time[1]) + 1) * 30) * 24 # hours
		hours_days = int(time[2]) * 24 # hours

		return (hours_year * 60) + (hours_month * 60) + (hours_days * 60)

	unsorted_dirs = sorted(unsorted_dirs, key=sum_hours)

	for index, dir in unsorted_dirs:
		sleep(1)
		print(f"{index + 1}. {dir}")

if sys.argv[-1] == path:
	default_sort(path)
else:
	option = sys.argv[2]

	if option == '--dry-run':
		dry_run(path)

	elif option == '--by-date':
		by_date(dirs, path)













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