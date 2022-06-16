# -*- coding: utf-8 -*-
import codecs
import time as t
import sys
import bot_response_lib as brl
import random as r


love     = brl.all_love
non_love = brl.all_non_love


#jap1 = "こんにちは"
#jap2 = "こんにち"
#print(jap1 == jap1)
#print(jap1 == jap2)

## Japanese argument equality testing working
#try:
#    print(sys.argv[1] == sys.argv[2])
#except:
#    print("not enough inputs")

jap1 = ''
try:
    jap1 = sys.argv[1]
except:
    jap1 = ''

rlove = r.random()

buff = ''
val = None
if (rlove > 0.8):
    val = love
else:
    val = non_love


i   = r.randint(0,len(val)-1)
ii  = r.randint(0,len(val[i])-1)
val1 = val[i]
val2 = val1[ii]
buff = val2

print(buff)
