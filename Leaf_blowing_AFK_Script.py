import pyautogui as pgui
import keyboard as kb
import colorama as c
from time import sleep
import os
import ctypes
pgui.FAILSAFE = False
User = ctypes.windll.user32
xVal = User.GetSystemMetrics(0)
yVal = User.GetSystemMetrics(1)
os.system("cls")
#VARIABLES && BANNERS
banner = c.Fore.RED + c.Back.GREEN +"""

██╗     ██████╗ ██████╗                               
██║     ██╔══██╗██╔══██╗                              
██║     ██████╔╝██████╔╝                              
██║     ██╔══██╗██╔══██╗                              
███████╗██████╔╝██║  ██║                              
╚══════╝╚═════╝ ╚═╝  ╚═╝                              
                                                      
 █████╗ ███████╗██╗  ██╗    ██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║█████╗  █████╔╝     ██████╔╝██║   ██║   ██║   
██╔══██║██╔══╝  ██╔═██╗     ██╔══██╗██║   ██║   ██║   
██║  ██║██║     ██║  ██╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                      
"""
VerHor = """
||||||||||
||||||||||
||||||||||
↓↓↓↓↓↓↓↓↓↓
(1) (Low && Medium blowing power for maximum efficiency)
"""
HorVer = """
---------→
---------→
---------→
---------→
(2) (Medium Blowing power for maximum efficiency)
"""

CentreSquare = """
---------→
         |
↑----→   |
|        ↓
←---------
(3) (High Blowing power for maximum efficiency)
"""
#SEQUENCES
#LOW POWER
def VerHorSequence():
    i = 0
    while True:
        for x in range(10):
            for y in range(2):
                if i % 2 == 0:
                    pgui.moveTo(((xVal/10)*(x)),((yVal/10)))
                    i+=1
                else:
                    pgui.moveTo(((xVal/10)*(x)),((yVal/10)*9))
                    i+=1
                sleep(0.1)
                
        if kb.is_pressed("e"):
            print("Stop key pressed!")
            break
#MEDIUM POWER
def HorVerSequence():
    while True:
        for y in range(4):
            for x in range(6):
                print((xVal/6)*x)
                print((yVal/4)*y)
                pgui.moveTo(((xVal/6)*(x))+30,((yVal/4)*(y))+20)
                sleep(0.1)
                
        if kb.is_pressed("e"):
            print("Stop key pressed!")
            break
#HIGH POWER           
def CentreSquareSequence():
    #1/10 of screen size
    x10 = xVal/10
    y10 = yVal/10
    while True:
        #coordinates for this sequence ( also timings )
        pgui.moveTo(x10,y10,0.2)
        pgui.moveTo((x10*9),y10,0.2)
        pgui.moveTo((x10*9),(y10*9),0.2)
        pgui.moveTo(x10,(y10*9),0.2)
        pgui.moveTo(x10,(y10*5),0.2)
        pgui.moveTo((x10*9),(y10*5),0.5)
        if kb.is_pressed("e"):
            print("Stop key pressed!")
            break



#MAIN FUNCTION (MANAGER)
def menu():
    print(banner+c.Style.RESET_ALL)
    sleep(5)
    os.system("cls")
    print(c.Fore.GREEN+VerHor)
    print(c.Fore.GREEN+HorVer)
    print(c.Fore.GREEN+CentreSquare)
    main = int(input("What settings do you want, when AFK-ing? (1,2,3) >> "))
    if main == 1:
        print("The program will start afk-ing in 5 seconds! Please open leaf blowing simulator in fullscreen, with no menus open. To exit, press e (hold e until the script does a full cycle")
        sleep(5)
        VerHorSequence()
    elif main == 2:
        print("The program will start afk-ing in 5 seconds! Please open leaf blowing simulator in fullscreen, with no menus open. To exit, press e (hold e until the script does a full cycle")
        sleep(5)
        HorVerSequence()
    elif main == 3:
        print("The program will start afk-ing in 5 seconds! Please open leaf blowing simulator in fullscreen, with no menus open. To exit, press e (hold e until the script does a full cycle")
        sleep(5)
        CentreSquareSequence()
    else:
        print("Incorrect value!")
    

menu()
