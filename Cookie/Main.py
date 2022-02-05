from calendar import c
import pyautogui
import time

def moveCookie():  
    pyautogui.moveTo(300, 400, duration = .04)
    time.sleep(0)
    pyautogui.PAUSE = 0.0001 
    pyautogui.click()

def clickUpgrade():
    for i in range(3):
        pyautogui.moveTo(1800, 215, duration = 0.2)
        pyautogui.click()

def upgradeClick():  
    pyautogui.moveTo(1800, 800, 1)
    pyautogui.PAUSE = 0.00001
    time.sleep(0.3)
    for i in range(9):
        for i in range(5):
            pyautogui.click()
        pyautogui.moveRel(0, -65, .3)

def oneKC():
    time.sleep(0)
    pyautogui.PAUSE = 0.0001
    for i in range(2000):
        moveCookie()
    goldenCookie()

def boost():
    boostcorner = pyautogui.locateOnScreen('img/boostcorner.png')
    if not boostcorner:
        money()
    else:
        pyautogui.moveTo(1630, 110, 0.4)
        pyautogui.click()
        upgrade()

def goldenCookie():
    color = (119, 79, 46)

    s = pyautogui.screenshot()
    x = 0
    
    while x < s.width:
        y = 0
        while y < s.height:
            if s.getpixel((x, y)) == color:
                pyautogui.click(x, y)
                print('found it!')
                return
            y += 3
        x += 3
print("LOSER")


def achievement():
    pyautogui.moveTo(1110, 1010, 0.3)
    pyautogui.click()

def money():
    for i in range(5):
        oneKC()
    print('Iraq')
    boost()

def seekBoost():
    boostcorner = pyautogui.locateOnScreen('img/boostcorner.png')
    print(boostcorner)

def upgrade():
    pyautogui.PAUSE = 0.0001
    for i in range(10):
        oneKC()
        achievement()
        upgradeClick()
        clickUpgrade()
    boost()

upgrade()



