from calendar import c
import pyautogui
import time

#Detects if you have enough to buy a boost
boostcorner = pyautogui.locateOnScreen('img/boostcorner.png')

#move to cookie and click
def moveCookie():  
    pyautogui.moveTo(300, 400, duration = .04)
    time.sleep(0)
    pyautogui.PAUSE = 0.0001 
    pyautogui.click()

#attempt to buy CURSOR upgrade 3 times
#fixes a weird bug when added at the end of 'upgrade'
def clickUpgrade():
    for i in range(3):
        pyautogui.moveTo(1800, 215, duration = 0.2)
        pyautogui.click()

#attempts to buy each upgrade 5 times
#doesn't buy CURSOR upgrade for some reason (fixed with clickUpgrade)
def upgradeClick():  
    pyautogui.moveTo(1800, 800, 1)
    pyautogui.PAUSE = 0.00001
    time.sleep(0.3)
    for i in range(9):
        for i in range(5):
            pyautogui.click()
        pyautogui.moveRel(0, -65, .3)

#Click 2k times and check for Golden Cookies
def oneKC():
    time.sleep(0)
    pyautogui.PAUSE = 0.0001
    for i in range(2000):
        moveCookie()
    goldenCookie()

#attempts to buy furthest left boost 3 times
#Sometimes image search breaks so I put a failsafe to attempt to buy anyways and rotate back to 'Upgrade' if it can't find it after a while
def boost():
    boostcorner = pyautogui.locateOnScreen('img/boostcorner.png')
    if not boostcorner:
        print('broke mf') #tells you that you are too broke to buy a boost or it can't see the boost. stupid computer doesn't know if I'm broke or if it's blind...
        for i in range(15):
            money()
        pyautogui.moveTo(1630, 110, 0.4)
        pyautogui.click()
        upgrade()
    else:
        for i in range(3):
            pyautogui.moveTo(1630, 110, 0.4)
            pyautogui.click()
        upgrade()

#Color Matches for Golden Cookie
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
                for i in range(3):
                    oneKC()
                return
            y += 3
        x += 3
print("LOSER") #this is funny because I accidentally tabbed this back instead of deleting it but the script calls you a loser for no reason immediately everytime you run it lol.

#clears achievements bc they are annoying. only works if there are two or more which is kinda dumb but I'm too lazy to change it.
def achievement():
    pyautogui.moveTo(1110, 1010, 0.3)
    pyautogui.click()

#Meant to sit and make a bunch of cookies in anticipation of buying a boost.
#clicks cookie a lot and checks for a boost to be buyable.
#Idk why it prints Iraq but I'm leaving it. The point is up for interpretation I suppose.
def money():
    for i in range(2):
        oneKC()
        if boostcorner:
           pyautogui.moveTo(1630, 110, 0.4)
           pyautogui.click()
           upgrade() 
    print('Iraq') #finished grinding money. either bought boost or was too broke.

#this finds a buyable boost and prints its coords.
#I don't know why this is here but maybe I'll use it at some point idk.
def seekBoost():
    boostcorner = pyautogui.locateOnScreen('img/boostcorner.png')
    print(boostcorner)

#basically the Main function for some reason not called main.
#Infinite loop that plays the game.
#clicks the cookie a bunch, clears achievements, buys upgrades, repeats 30 times,then runs boost().
def upgrade():
    pyautogui.PAUSE = 0.0001
    for i in range(30):
        oneKC()
        achievement()
        upgradeClick()
        clickUpgrade()
    print("Boostin'") #attempting to buy a boost.
    boost()

#this can be replaced with upgrade() but I start it here so that if I have enough money for a boost is buys it instead of upgrades when I run the script.
boost()



