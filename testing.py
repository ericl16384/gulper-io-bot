import time
import cv2
import pyautogui
# import numpy as np
import numpy_vectors as npv
import mss
import keyboard
import sys
import math
from PIL import ImageGrab


START_KEY = "insert"
EMERGENCY_STOP_KEY = "ctrl"
STARTUP_TIMEOUT = 30

MIN_LOOP_PERIOD = 1 / 60

SCREEN_SIZE = (pyautogui.size()[0], pyautogui.size()[1])
SCREEN_CENTER = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)

# # region to capture (left, top, right, bottom)
game_region = (100, 100, SCREEN_SIZE[0]-100, SCREEN_SIZE[1]-100)
def get_center_of_game_region():
    return (
        (game_region[0] + game_region[2]) / 2,
        (game_region[1] + game_region[3]) / 2
    )


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



def get_screenshot(region=None):
    return ImageGrab.grab(region)



def get_desired_direction():
    t = (time.time() % (2*math.pi))
    # print(t)
    d = (math.cos(t), math.sin(t))
    return npv.normalize(npv.to_vector(d))


def main():
    print(f"awaiting keyboard input '{START_KEY}' to start the loop")
    print(f"awaiting keyboard input '{EMERGENCY_STOP_KEY}' to stop the loop")

    end_time = time.time() + STARTUP_TIMEOUT
    while not keyboard.is_pressed(START_KEY):
        handle_emergency_stop()
        time.sleep(0.001)
        if time.time() >= end_time:
            global EMERGENCY_STOP_ACTIVE
            EMERGENCY_STOP_ACTIVE = True
            print(f"startup timed out {STARTUP_TIMEOUT}s")

    while True:
        iteration_end_time = time.time() + MIN_LOOP_PERIOD


        handle_emergency_stop()


        screenshot = get_screenshot(game_region)
        

        handle_emergency_stop()


        # # not instant!
        # pyautogui.moveTo(game_center[0] + 50, game_center[1])
        # pyautogui.click()

        mouse_pos = npv.vector_to_int_tuple(get_desired_direction() * 300 + get_center_of_game_region())

        pyautogui.moveTo(*mouse_pos)


        handle_emergency_stop()
        
        
        while time.time() < iteration_end_time:
            handle_emergency_stop()
            time.sleep(0.001)


if __name__ == "__main__":
    main()
