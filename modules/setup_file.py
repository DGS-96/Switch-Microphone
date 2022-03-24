from os import path

def check_setup(setup_file_path):
	return path.exists(setup_file_path)


def create_setup(setup_file_path):
	setup_file = open(setup_file_path, "w")
	print("microphone_position = 1", file=setup_file)
	setup_file.close()


def read_setup(setup_file_path):
	setup_file = open(setup_file_path, "r")
	temp = setup_file.read().replace("\n", "")
	microphone_position = int(temp.split("=")[1].strip())
	setup_file.close()
	del temp
	return microphone_position	


if __name__ == "__main__":
	from os import environ
	setup_file_path = environ["USERPROFILE"] + r"\Documents\Switch-Microphone_Setup.txt"

	print(read_setup(setup_file_path))
	print(type(read_setup(setup_file_path)))
