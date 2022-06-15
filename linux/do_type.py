# -*- coding: utf-8 -*-
import codecs
import pyautogui as pa
import time as t
import sys


t.sleep(5)

def type_unicode2(word):
    for char in word:
        num = hex(ord(char))
        pa.hotkey('ctrl', 'shift', 'u')
        for n in num:
            pa.typewrite(n)
        pa.typewrite('\n')

def type_unicode(word):
    for c in word:
        c = '%04x' % ord(c)
        pa.keyDown('optionleft')
        pa.typewrite(c)
        pa.keyUp('optionleft')

#pa.typewrite(str(sys.argv))
#pa.typewrite("robots are awesome")
jap1 = "こんにちは"
jap2 = "こんにち"
print(jap1 == jap1)
print(jap1 == jap2)
type_unicode2(jap1)
pa.press('enter')
#theOut = codecs.open(jap1,'r','utf-8')
#pa.typewrite("こんにちは")
