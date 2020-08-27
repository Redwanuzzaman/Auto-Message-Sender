# this will send a message 10 times to a user with a break of 3 seconds.

import pyautogui as pg  # import the package pyautogui

for i in range(10):
    pg.typewrite('I send this message automatically. :D')  # this is the message you want to send
    pg.press('enter')  # the keyboard button we press to send
    pg.sleep(3)  # this will wait for 3 seconds to send another message
