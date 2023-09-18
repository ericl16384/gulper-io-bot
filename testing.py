import time
import cv2
import pyautogui
import numpy as np
import mss
import keyboard
import sys


START_KEY = "ctrl_r"
EMERGENCY_STOP_KEY = "f"

MIN_LOOP_PERIOD = 0.5

game_region = {"top": 300, "left": 300, "width": 800, "height": 600}


EMERGENCY_STOP_ACTIVE = False

def handle_emergency_stop():
    if EMERGENCY_STOP_ACTIVE:
        print("stopping though handle_emergency_stop()")
        sys.exit()

def _emergency_stop_trigger(e):
    if keyboard.is_pressed(EMERGENCY_STOP_KEY):
        global EMERGENCY_STOP_ACTIVE
        EMERGENCY_STOP_ACTIVE = True
        
        # exiting here doesn't work :(
        # the below doesn't work :(((

        # print("stopping though _emergency_stop_trigger()")
        # sys.exit()

        # handle_emergency_stop()

keyboard.on_press(_emergency_stop_trigger)



def get_center_of_game_screen(game_region):
    return (game_region["left"] + game_region["width"] // 2, game_region["top"] + game_region["height"] // 2)



def get_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output="screenshot.png")

    return cv2.imread(filename)


def limit_loop_speed():
    end_time = time.time() + MIN_LOOP_PERIOD
    while time.time() < end_time:
        time.sleep(0.001)
        handle_emergency_stop()

def main_loop():
    while True:
        handle_emergency_stop()
        # if keyboard.is_pressed(EMERGENCY_STOP_KEY):

        # Read the captured screen
        screen = get_screenshot()
        
        game_center = get_center_of_game_screen(game_region)
        
        handle_emergency_stop()

        # not instant!
        pyautogui.moveTo(game_center[0] + 50, game_center[1])
        pyautogui.click()

        handle_emergency_stop()
        
        limit_loop_speed()


if __name__ == "__main__":
    main_loop()
