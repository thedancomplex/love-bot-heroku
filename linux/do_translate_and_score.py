# -*- coding: utf-8 -*-
import codecs
import time as t
import sys
from googletrans import Translator
from textblob import TextBlob as tb



translator = Translator()



jap1 = None

try:
    jap1 = sys.argv[1]
except:
    exit(1)

translated_text = translator.translate(jap1)
#translated_text = translator.translate(jap1,dest='en',src='ja')

#print(translated_text.text)
text = tb(translated_text.text)
#print(text)
#print(text.sentiment)
print('%1.3f %1.3f' % (text.sentiment.polarity, text.sentiment.subjectivity))


