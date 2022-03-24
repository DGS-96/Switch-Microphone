from os import system
from time import sleep
from pyautogui import PAUSE, FAILSAFE
from pyautogui import hotkey, press


pause_time = 0.2

# pyautogui setup
PAUSE = pause_time
FAILSAFE = True


def turn_on(microphone_position):
	global pause_time
	
	system("mmsys.cpl")
	sleep(pause_time)

	hotkey("ctrl", "tab")

	for _ in range(microphone_position):
		press("down")

	hotkey("shift", "f10")
	press("down")
	press("enter")
	press("enter")


def turn_off(microphone_position):
	global pause_time
	
	system("mmsys.cpl")
	sleep(pause_time)

	hotkey("ctrl", "tab")
	
	for _ in range(microphone_position):
		press("down")
	
	hotkey("shift", "f10")
	press("down")
	press("down")
	press("enter")
	press("enter")


if __name__ == "__main__":
	test_microphone_position = 1
	
	turn_on(test_microphone_position)
	sleep(pause_time)
	turn_off(test_microphone_position)
