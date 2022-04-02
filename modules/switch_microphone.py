from os import system
from time import sleep
from pyautogui import PAUSE, FAILSAFE
from pyautogui import hotkey, press


# Wait to open "mmsys.cpl" in windows
sleep_time = 0.3

# pyautogui setup
PAUSE = 0.1
FAILSAFE = True


def turn_on(microphone_position):
	global sleep_time
	
	system("mmsys.cpl")
	sleep(sleep_time)

	# Next tab
	hotkey("ctrl", "tab")

	for _ in range(microphone_position):
		press("down")

	# Options
	hotkey("shift", "f10")
	
	press("down")
	press("enter")
	press("enter")


def turn_off(microphone_position):
	global sleep_time
	
	system("mmsys.cpl")
	sleep(sleep_time)

	# Next tab
	hotkey("ctrl", "tab")
	
	for _ in range(microphone_position):
		press("down")
	
	# Options
	hotkey("shift", "f10")
	
	press("down")
	press("down")
	press("enter")
	press("enter")


if __name__ == "__main__":
	test_microphone_position = 1
	
	turn_on(test_microphone_position)
	sleep(sleep_time)
	turn_off(test_microphone_position)
