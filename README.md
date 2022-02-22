# Switch-Microphone
Simple microphone switching script. Turns the microphone on/off in __Control panel\Sound settings__
<br>Python 3.9

# Download build
[For Windows](https://codeload.github.com/DGS-96/Switch-Microphone/zip/refs/heads/build)

# Installation
### Clone repository
```
git clone https://github.com/DGS-96/Switch-Microphone.git
```
### Change the working directory to Pomodoro-Timer
```
cd Switch-Microphone
```
### Install the requirements
```
python3 -m pip install -r requirements.txt
```

# Usage
1. Before the first start, the microphone must be turned on in __Control panel\Sound settings__
1. Run file __Switch-Microphone.exe__. On first run, two files will be created:
   - __\USERPROFILE\Documents\Switch-Microphone-Setup.txt__ in which you need to specify the position of the microphone, which can be viewed in 
   <br>__Control panel\Sound settings__
   - __\USERPROFILE\Desktop\Microphone On.txt__ which serves as an indicator of the switched on microphone
1. The next time you start the application:
   - if the microphone is on, the microphone will be turned off and the file on the desktop will be deleted
   - if the microphone is off, the microphone will be enabled and an indicator file will be created on the desktop
