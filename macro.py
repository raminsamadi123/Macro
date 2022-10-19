# Importing libraries
from asyncore import write
import code
from platform import python_branch
import pyautogui
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
pyautogui.FAILSAFE = False
from pynput import keyboard, mouse


# -----MOUSE SECTION-----

# What to do when the mouse moves
def lobby():
    pyautogui.PAUSE = 1.5 
    pyautogui.leftClick(1796, 1032) #Play
    
    pyautogui.PAUSE = 1.5 
    pyautogui.leftClick(1185, 427) #Hero Raid
    
    pyautogui.PAUSE = 1.5 
    pyautogui.leftClick(998, 392) #Private
    
    pyautogui.PAUSE = 1.5 
    pyautogui.leftClick(1291, 813) #Confirm
    
    pyautogui.PAUSE = 10 
    pyautogui.leftClick(999, 780) #Start

def map_selection():
    pyautogui.PAUSE = 10
    pyautogui.leftClick(796, 614) #The City

def enable_equipment():
    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(90, 203) #Menu icon
    
    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(88, 267) #Assignment icon

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(1264, 547) #Inventory

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(959, 472) #Open Armor Menu

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(827, 376) #Select Giant Horns

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(1113, 757) #Equip Giant Horns

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(1237, 308) #Exit Armor & Gadgets

    pyautogui.PAUSE = 1.5
    pyautogui.leftClick(1139, 322) #Exit Inventory

def auto_grind():
    pyautogui.PAUSE = 1
    pyautogui.press("z")
    i = 0
    minute = 120

    while i != (minute * 30): #For longer grinding change the number multiplied by minutes
        pyautogui.press("x")
        pyautogui.press("v")
        i = i + 2
        pyautogui.PAUSE = 0.5 #0.5 seconds delay between each loop

def end_grind():
    pyautogui.PAUSE = 1.5
    pyautogui.press("esc")

    pyautogui.PAUSE = 1.5
    pyautogui.press("r")

    pyautogui.PAUSE = 30
    pyautogui.press("enter")

# What to do when a button on the mouse is clicked
def on_click(x, y, button, pressed):
    if button == mouse.Button.middle:
        while True:
            lobby()
            map_selection()
            enable_equipment()
            auto_grind()
            end_grind()



# COLLECTING EVENTS...
mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()
mouse_listener.join()

# TEST TYPING:
