# -*- coding: utf-8 -*-
import codecs
import pyautogui as pa
import time as t
import sys



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

## Comparing two strings working
jap1 = "こんにちは"
jap2 = "こんにち"
print(jap1 == jap1)
print(jap1 == jap2)

## Japanese argument equality testing working
#try:
#    print(sys.argv[1] == sys.argv[2])
#except:
#    print("not enough inputs")

try:
    jap1 = sys.argv[1]
except:
    exit(1)


#type in the active window
the_out = jap1
type_unicode2(the_out)
pa.press('enter')
#theOut = codecs.open(jap1,'r','utf-8')
#pa.typewrite("こんにちは")
