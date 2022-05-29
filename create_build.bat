mkdir build
cd build
pyinstaller -F -w -i "%~dp0icon.ico" --paths "%~dp0modules" "%~dp0main.py"
cd dist
ren "main.exe" "Switch Microphone.exe"
pause