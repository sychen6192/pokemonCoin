import pyautogui, time, keyboard, datetime
from multiprocessing import Process, Value


def catchImageClick(img):
    pyautogui.click((pyautogui.locateCenterOnScreen(img)))


def getPosition(img):
    s = pyautogui.locateOnScreen(img, confidence=0.9)
    pyautogui.moveTo(s.left+s.width//2, s.top+s.height//2)
    return s.left+s.width//2, s.top+s.height//2


def moveTo(x, y):
    pyautogui.moveTo(x, y)


def drag(x, y):
    pyautogui.drag(x, y, 0.5, button='left')


def lockToCloseButtom():
    tmp = pyautogui.locateOnScreen('./image/dojo.png', confidence=0.9)
    return tmp.left - 50, tmp.left + tmp.width


def pressTostart():
    while True:
        if keyboard.read_key() == "s":
            print("Start...")
            break


if __name__ == '__main__':
    pressTostart()
    while True:
        x_org, y_org = getPosition('./image/poke.png')
        l_pad, r_pad = lockToCloseButtom()

        catchImageClick('./image/battle.png')

        while not (pyautogui.locateOnScreen('./image/ad.png')\
                   or pyautogui.locateOnScreen('./image/ok.png')
                   or pyautogui.locateOnScreen('./image/bigOK.png')):
            moveTo(x_org + 20, y_org)
            drag(0, -100)

        if pyautogui.locateOnScreen('./image/ad.png'):
            catchImageClick('./image/ad.png')
            time.sleep(7)
            if pyautogui.locateOnScreen('./image/pokeAd.png'):
                catchImageClick('./image/pokeAd.png')
            elif pyautogui.locateOnScreen('./image/yes.png'):
                catchImageClick('./image/yes.png')
            else:
                while not pyautogui.locateOnScreen('./image/closeAd.png')\
                        or pyautogui.locateOnScreen('./image/closeAd.png').left < l_pad\
                        or pyautogui.locateOnScreen('./image/closeAd.png').left > r_pad:
                    time.sleep(1)
                catchImageClick('./image/closeAd.png')

        elif pyautogui.locateOnScreen('./image/bigOK.png'):
            catchImageClick('./image/bigOK.png')

        else:
            catchImageClick('./image/ok.png')

        count = 0
        while not (pyautogui.locateOnScreen('./image/poke.png')):
            time.sleep(1)
            count += 1
            if count > 10:
                pyautogui.press('f5')
                time.sleep(60)
