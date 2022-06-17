# -*- coding: utf-8 -*-
import codecs
import time as t
import sys
from googletrans import Translator

translator = Translator()



jap1 = None
try:
    jap1 = sys.argv[1]
except:
    pass

try:
    translated_text = translator.translate(jap1)
    #translated_text = translator.translate(jap1,dest='en',src='ja')

    print(translated_text.text)
except:
    exit(1)



