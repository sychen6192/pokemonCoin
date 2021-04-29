import pyautogui, time


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


if __name__ == '__main__':
    while True:
        x_org, y_org = getPosition('./image/poke.png')
        print(x_org, y_org)

        catchImageClick('./image/battle.png')

        while not (pyautogui.locateOnScreen('./image/ad.png') or pyautogui.locateOnScreen('./image/ok.png')):
            moveTo(x_org+20, y_org)
            drag(0, -100)

        if pyautogui.locateOnScreen('./image/ad.png'):
            catchImageClick('./image/ad.png')
            time.sleep(90)
            catchImageClick('./image/closeAd.png')


        else:
            catchImageClick('./image/ok.png')

        while not (pyautogui.locateOnScreen('./image/poke.png')):
            time.sleep(1)