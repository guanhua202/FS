# ———————————————————— 🗂️ Органайзер файлов
# o Находить абсолютный путь ведённой папки
# ✅ 2. Дать возможность выводить список подпапок
# ✅ 3. Дать возможность отфильтровывать вывод подпапок по 3-м опциям: дата/расширение/размер
	# 	✅ По расширению
	# 	✅ По размеру
	# 	✅ По дате

import os
import sys
from time import sleep
from time import ctime

print('\n—————————————— 🗂️ Органайзер файлов\n')

# path = sys.argv[1] # Format write: ~/FolderName/

while os.path.exists(sys.argv[1]) == False:
	os.chdir(os.environ['HOME'])
	print("Write path not found.")

	if input("Repeat? (Y/N): ") == 'Y':
		sys.argv[1] = input("Write real path (Format write '~/FolderName/'): ")
	else:
		print('Bye')
		sys.exit()

files = os.listdir(path)

sys.argv.append('--type')

mode = sys.argv[2]
# text_formats = ['.txt', '.py', '.log', '.docx', '.doc', '.pdf', '.html']

def default_sort(unsorted_files,path):
	display_text("ТИПУ ФАЙЛА", path)

	files = sorted(unsorted_files, key=lambda file: os.path.splitext(file)[-1])

	for index, file in enumerate(files):
		sleep(1)
		print(f"{index + 1}. {file}")

def dry_run(unsorted_files, path):
	display_text("умолчанию (беспорядочный вывод)", path)
	total_dir = True
	for index, file in enumerate(unsorted_files):
		
		sleep(1)
		if os.path.isdir(file) and os.listdir(file) != []:
			print(f"{index + 1}. {file} ———>", *os.listdir(file))
		else:
			print(f"{index + 1}. {file}")

def by_date(unsorted_files, path):
	display_text("ДАТЕ ИЗМЕНЕНИЯ", path)

	def sum_hours(file):
		time = ctime(os.path.getmtime(file)).split()
		months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',]

		# Полный перевод в минуты из формата: Wed Sep 16 23:50:14 2026
		summ_minutes = (((int(time[4]) * 365) * 24) * 60) + ((((months.index(time[1]) + 1) * 30) * 24) * 60) + ((int(time[2]) * 24) * 60)
		minutes = [int(t) for t in time[3].split(':')]

		return summ_minutes + (minutes[0] * 60) + minutes[1]

	sort_files = sorted(unsorted_files, key=sum_hours)

	for index, file in enumerate(sort_files):
		sleep(1)
		print(f"{index + 1}. {file.ljust(len(max(sort_files, key=len)))} | {ctime(os.path.getmtime(file))}")

def by_size(unsorted_files, path):
	display_text("РАЗМЕРУ", path)

	sort_files = sorted(unsorted_files, key=lambda file: os.path.getsize(file))

	for index, file in enumerate(sort_files):
		sleep(1)
		print(f"{index + 1}. {file.ljust(len(max(sort_files, key=len)))} | {round(os.path.getsize(file) / 1024, 2)}KB")

def display_text(filter_name, path):
	print(f'Вы выбрали фильтрацию по {filter_name} из {path}')
	sleep(0.5)
	print('Ожидайте...')

modes = {
	'--type': 	 default_sort,
	'--dry-run': dry_run,
	'--by-date': by_date,
	'--by-size': by_size,
}

modes[mode](files, path)