# ———————————————————— 🗂️ File Sorter
# ✅ Create dirs in main PATH
# ✅ Move the photos to the Images folder and the videos to the Videos folder
# ✅ Move the txt file to the TXT and the code to the Code folder
# o Add function reset a last changes:
# 	o 

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

new_dirs = ['Images', 'Videos', 'TXT', 'Code']
files = os.listdir(path)
os.chdir(path)

sys.argv.append('--type')

mode = sys.argv[2]

with open('before_last_changes.log', 'a+') as log_file:
		for dir in files:
			log_file.write(dir + " ")

def default_sort(unsorted_files,path):
	display_text("TYPE FILE", path)

	files = sorted(unsorted_files, key=lambda file: os.path.splitext(file)[-1])

	images = ['.jpg', '.png', '.gif']
	videos = ['.mp4', '.webp']
	txt = ['.txt', '.docx']
	code = ['.py', '.html', '.css', '.js', '.sh', '.cpp', '.cs', '.php']

	os.makedirs('Images', exist_ok=True)
	os.makedirs('Videos', exist_ok=True)
	os.makedirs('TXT', exist_ok=True)
	os.makedirs('Code', exist_ok=True)
	os.makedirs('Dirs', exist_ok=True)

	for index, file in enumerate(files):
		sleep(1)
		print(f"{index + 1}. {file.ljust(len(max(unsorted_files, key=len)))} | {'Dir' if os.path.splitext(file)[1] == '' else os.path.splitext(file)[1]	}")

		if file not in new_dirs:
			if os.path.splitext(file)[1] in images:
				os.replace(file, f'Images/{file}')
			elif os.path.splitext(file)[1] in videos:
				os.replace(file, f'Videos/{file}')
			elif os.path.splitext(file)[1] in txt:
				os.replace(file, f'TXT/{file}')
			elif os.path.splitext(file)[1] in code and file != sys.argv[0]:
				os.replace(file, f'Code/{file}')
			elif os.path.splitext(file)[1] == '':
				os.replace(file, f'Dirs/{file}')

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

def reset_last_changes(files, path):
	screenshot = []

	with open('before_last_changes.log') as log_file:
		screenshot = log_file.readlines()

	for index, dir in enumerate(new_dirs):
		last_path = os.getcwd()
		
		if os.path.isdir(dir):
			
			for file in screenshot:
				if file in os.listdir(dir):
					os.chdir(dir)
					os.replace(file, f'{last_path}/{file}')
					os.chdir(last_path)

def display_text(filter_name, path):
	print(f'You select sorted filter by {filter_name} из {path}')
	sleep(0.5)
	print('One second...')

modes = {
	'--type': 	 default_sort,
	'--dry-run': dry_run,
	'--by-date': by_date,
	'--by-size': by_size,
	'--reset-last-changes': reset_last_changes,
}

modes[mode](files, path)
