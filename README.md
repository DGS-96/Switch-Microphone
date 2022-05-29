# Switch-Microphone
Simple microphone switching script. Turns the microphone on/off in **Control panel\Sound settings\Recording**\
Python 3.9

# Download build
[For Windows](https://codeload.github.com/DGS-96/Switch-Microphone/zip/refs/heads/build)

# Installation
### Clone repository
	git clone https://github.com/DGS-96/Switch-Microphone.git

### Change the working directory to Switch-Microphone
	cd Switch-Microphone

### Install the requirements
	python3 -m pip install -r requirements.txt

### Build .exe file
	create_build

# Usage
1. Before the first start, the microphone must be turned on in **Control panel\Sound settings\Recording**
1. Run file **Switch-Microphone.exe**. On first run, two files will be created:
   - **\USERPROFILE\Documents\Switch-Microphone-Setup.txt** in which you need to specify the position\
   of the microphone, which can be viewed in **Control panel\Sound settings\Recording**
   - **\USERPROFILE\Desktop\Microphone On.txt** which serves as an indicator of the switched on microphone
1. The next time you start the application:
   - if the microphone is on, the microphone will be turned off and the file on the desktop will be deleted
   - if the microphone is off, the microphone will be enabled and an indicator file will be created on the desktop
1. If the microphone position in the **\USERPROFILE\Documents\Switch-Microphone-Setup.txt** is incorrect,\
   the program will overwrite the setting and you need to specify the microphone position
