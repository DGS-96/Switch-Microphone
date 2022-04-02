from os import remove


def create(indicator_file_path):
	file = open(indicator_file_path, "w")
	file.close()


def delete(indicator_file_path):
	remove(indicator_file_path)


if __name__ == "__main__":
	indicator_file_path = r"C:\Users\Administrator\Desktop\Microphone On.txt"

	create(indicator_file_path)
	delete(indicator_file_path)
