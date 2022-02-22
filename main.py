from os import environ, remove, path
import switch_microphone
import setup_file


userprofile = environ["USERPROFILE"]
indicator_file_path = userprofile + r"\Desktop\Microphone On.txt"
setup_file_path = userprofile + r"\Documents\Switch-Microphone-Setup.txt"


if setup_file.check(setup_file_path):
	microphone_position = setup_file.read(setup_file_path)

	if path.exists(indicator_file_path):
		switch_microphone.turn_off(microphone_position)
		remove(indicator_file_path)
	else:
		switch_microphone.turn_on(microphone_position)
		file = open(indicator_file_path, "w")
		file.close()

else:
	setup_file.create(setup_file_path)
	file = open(indicator_file_path, "w")
	file.close()
