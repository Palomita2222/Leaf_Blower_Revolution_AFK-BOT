import cv2
import numpy as np
from PIL import ImageGrab as ig
import pyautogui as pgui
import ctypes
User = ctypes.windll.user32
xVal = User.GetSystemMetrics(0)
yVal = User.GetSystemMetrics(1)
#You can modify the threshold if you want, but its already fine
threshold = 0.65
apple_threshold = 0.5

# IF YOU DONT KNOW WHAT YOU ARE DOING, JUST MODIFY THE SRC PART, TO THE CORRESPONDING IMAGES BELOW
gun = cv2.imread(r"SRC HERE", cv2.IMREAD_UNCHANGED)
apple = cv2.imread(r"SRC HERE", cv2.IMREAD_UNCHANGED)
golden_apple = cv2.imread(r"SRC HERE")
platinum_apple = cv2.imread(r"SRC HERE")
# DO NOT MODIFY ANYTHING ELSE (if you dont know what you're doing)
while True:

    #SCREEN
    #screen_gun = ig.grab(bbox=(200,1250,300,1350))
    screen_apple = ig.grab(bbox=(0,0,xVal-1,yVal-1)) #Fullscreen  for searching for apples

    #ADAPT FOR cv2
    #np_screen_gun = np.array(screen_gun)
    np_screen_apple = np.array(screen_apple)

    #FIX_COLOR
    #np_screen_gun = cv2.cvtColor(np_screen_gun, cv2.COLOR_RGB2BGR)
    np_screen_apple = cv2.cvtColor(np_screen_apple, cv2.COLOR_RGB2BGR)
    resized = cv2.resize(np_screen_apple, (int(np_screen_apple.shape[1] * 50 / 100),int(np_screen_apple.shape[0] * 50 / 100)), interpolation = cv2.INTER_AREA)
    

    #TEMPLATE MATCHING (TM_CCOEFF_NORMED)
    #result_gun = cv2.matchTemplate(np_screen_gun, gun, cv2.TM_CCOEFF_NORMED)
    result_apple = cv2.matchTemplate(np_screen_apple, apple, cv2.TM_CCOEFF_NORMED)
    result_apple_golden = cv2.matchTemplate(np_screen_apple, golden_apple, cv2.TM_CCOEFF_NORMED)
    result_apple_platinum = cv2.matchTemplate(np_screen_apple, platinum_apple, cv2.TM_CCOEFF_NORMED)

    #GET POS && VAL of Template Match
    #min_val_gun, max_val_gun, min_loc_gun, max_loc_gun = cv2.minMaxLoc(result_gun)
    min_val_apple, max_val_apple, min_loc_apple, max_loc_apple = cv2.minMaxLoc(result_apple)
    min_val_apple_golden, max_val_apple_golden, min_loc_apple_golden, max_loc_apple_golden = cv2.minMaxLoc(result_apple_golden)
    min_val_apple_platinum, max_val_apple_platinum, min_loc_apple_platinum, max_loc_apple_platinum = cv2.minMaxLoc(result_apple_platinum)

    #GET METRICS (image metrics)
    """
    width_gun = gun.shape[1]
    height_gun = gun.shape[0]
    """
    width_apple = apple.shape[1]
    height_apple = apple.shape[0]
    width_apple_golden = golden_apple.shape[1]
    height_apple_golden = golden_apple.shape[0] 
    width_apple_platinum = platinum_apple.shape[1]
    height_apple_platinum = platinum_apple.shape[0]



    #IF CONDITIONALS WITH THRESHOLD (AKA IF TRUE)
    """
    if max_val_gun >= threshold:
        cv2.rectangle(np_screen_gun, max_loc_gun, (max_loc_gun[0]+width_gun, max_loc_gun[1]+height_gun), (255,0,255), 2)
    """
    #APPLES
    #NORMAL
    if max_val_apple >= apple_threshold:
        cv2.rectangle(resized, max_loc_apple, (max_loc_apple[0]+width_apple, max_loc_apple[1]+height_apple), (0,255,0), 3)
        pgui.click(max_loc_apple[0]+width_apple,max_loc_apple[1]+height_apple)
    #GOLDEN
    if max_val_apple_golden >= apple_threshold:
        cv2.rectangle(resized, max_loc_apple_golden, (max_loc_apple_golden[0]+width_apple_golden, max_loc_apple_golden[1]+height_apple_golden), (0,255,0), 3)
        pgui.click(max_loc_apple_golden[0]+width_apple_golden,max_loc_apple_golden[1]+height_apple_golden)
    #PLATINUM
    if max_val_apple_platinum >= apple_threshold:
        cv2.rectangle(resized, max_loc_apple_platinum, (max_loc_apple_platinum[0]+width_apple_platinum, max_loc_apple_platinum[1]+height_apple_platinum), (0,255,0), 3)
        pgui.click(max_loc_apple_platinum[0]+width_apple_platinum,max_loc_apple_platinum[1]+height_apple_platinum)
    #SHOW SCREEN(s)
    #cv2.imshow("MONITOR", np_screen_gun)
    cv2.imshow("Apple_cam", resized)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break