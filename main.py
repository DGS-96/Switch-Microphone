from os import environ, remove, path

# Import my modules
from modules import switch_microphone
from modules import indicator_file
from modules import setup_file


userprofile = environ["USERPROFILE"]
indicator_file_path = userprofile + r"\Desktop\Microphone On.txt"
setup_file_path = userprofile + r"\Documents\Switch-Microphone Setup.txt"


if setup_file.check_setup(setup_file_path):
	microphone_position = setup_file.read_setup(setup_file_path)

	if path.exists(indicator_file_path):
		switch_microphone.turn_off(microphone_position)
		indicator_file.delete(indicator_file_path)
	else:
		switch_microphone.turn_on(microphone_position)
		indicator_file.create(indicator_file_path)
		
else:
	# First run
	# Create setup file in user documents folder
	setup_file.create_setup(setup_file_path)
	indicator_file.create(indicator_file_path)
