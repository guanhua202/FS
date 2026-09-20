# ———————————————————— 🗂️ File Sorter
# ✅ Create dirs in main PATH
# ✅ Move the photos to the Images folder and the videos to the Videos folder
# o Move the txt file to the TXT and the code to the Code folder
# o Add function reset a last changes

import os
import sys
from time import sleep
from time import ctime

print('\n—————————————— 🗂️ File Sorter\n')

path = sys.argv[1] # Work PATH

while os.path.exists(sys.argv[1]) == False:
	print(f"Dir <{sys.argv[1]}> not found.")

	if input("Repeat? (Y/N): ") in 'Yy':
		sys.argv[1] = input("Write real path (Format write 'FolderName'): ")
	else:
		print('Bye')
		sys.exit()

	path = sys.argv[1]
else:
	path = sys.argv[1]

files = os.listdir(path)
os.chdir(path)

sys.argv.append('--type')

mode = sys.argv[2]

def default_sort(unsorted_files,path):
	display_text("TYPE FILE", path)

	files = sorted(unsorted_files, key=lambda file: os.path.splitext(file)[-1])
	images = ['.jpg', '.png', '.gif']
	videos = ['.mp4', '.webp']
	txt = ['.txt', '.docx']

	os.makedirs('Images', exist_ok=True)
	os.makedirs('Videos', exist_ok=True)

	for index, file in enumerate(files):
		sleep(1)
		print(f"{index + 1}. {file.ljust(len(max(unsorted_files, key=len)))} | {'Dir' if os.path.splitext(file)[1] == '' else os.path.splitext(file)[1]	}")

		if file != 'Images' and file != 'Videos':
			if os.path.splitext(file)[1] in images:
				os.replace(file, f'Images/{file}')
			elif os.path.splitext(file)[1] in videos:
				os.replace(file, f'Videos/{file}')

def dry_run(unsorted_files, path):
	display_text("умолчанию (беспорядочный вывод)", path)

	for index, file in enumerate(unsorted_files):
		sleep(1)
		if os.path.isdir(file) and os.listdir(file) != []:
			print(f"{index + 1}. {file} ———>", *os.listdir(file))
		else:
			print(f"{index + 1}. {file}")

def by_date(unsorted_files, path):
	display_text("CREATION/CHANGED/MODIFICATION", path)

	def sum_hours(file):

		time = ctime(os.path.getmtime(file)).split()
		months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',]

		# Translate the format time in minutes: Wed Sep 16 23:50:14 2026
		summ_minutes = (((int(time[4]) * 365) * 24) * 60) + ((((months.index(time[1]) + 1) * 30) * 24) * 60) + ((int(time[2]) * 24) * 60)
		minutes = [int(t) for t in time[3].split(':')]

		return summ_minutes + (minutes[0] * 60) + minutes[1]

	sort_files = sorted(unsorted_files, key=sum_hours)

	for index, file in enumerate(sort_files):
		sleep(0.5)
		print(f"{index + 1}. {file.ljust(len(max(sort_files, key=len)))} | {ctime(os.path.getmtime(file))}")

def by_size(unsorted_files, path):
	display_text("SIZE", path)

	sort_files = sorted(unsorted_files, key=lambda file: os.path.getsize(file))

	for index, file in enumerate(sort_files):
		sleep(0.5)
		print(f"{index + 1}. {file.ljust(len(max(sort_files, key=len)))} | {round(os.path.getsize(file) / 1024, 2)}KB")

def display_text(filter_name, path):
	print(f'You select sorted filter by {filter_name} из {path}')
	sleep(0.5)
	print('One second...')

modes = {
	'--type': 	 default_sort,
	'--dry-run': dry_run,
	'--by-date': by_date,
	'--by-size': by_size,
}

modes[mode](files, path)