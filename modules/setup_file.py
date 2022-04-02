import re
from os import path


def check_setup(setup_file_path):
	return path.exists(setup_file_path)


def create_setup(setup_file_path):
	setup_file = open(setup_file_path, "w")
	print("""\
Switch-Microphone script settings.
Link to source: https://github.com/DGS-96/Switch-Microphone\n
Microphone position = 1""", 
	file=setup_file)
	setup_file.close()


def read_setup(setup_file_path):
	setup_file = open(setup_file_path, "r")
	setup_data = setup_file.read()
	setup_file.close()

	temp = re.search(r"Microphone position = \d$", setup_data)
	if temp:
		# Microphone position
		return int(re.search(r"\d$", temp.group()).group())
	else:
		# Rewrite setup file
		create_setup(setup_file_path)


if __name__ == "__main__":
	setup_file_path = r"C:\Users\Administrator\Documents\Switch-Microphone Setup.txt"

	#print(check_setup(setup_file_path))
	#create_setup(setup_file_path)
	print(read_setup(setup_file_path))
