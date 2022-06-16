# Using readlines()
import codecs
file1 = codecs.open('jap_ocr.txt', 'r','utf-8')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
#for line in Lines:
#    count += 1
#    print("Line{}: {}".format(count, line.strip()))

#print(Lines)
#print(len(Lines))
try:
  buff = ''
  for i in range(len(Lines)):
#    print(Lines[i])
    Lines[i]=Lines[i].strip()
#    print(Lines[i])

  for i in range(len(Lines)-2,0,-1):
#    print("####")
#    print(i)
    l = Lines[i]
#    print(l)
#    print(len(l))
    buff = l + buff
#    print(buff)
    if (len(l) == 0):
#        print("break at")
#        print(i)
        break
    #print(len(Lines[i])
#    if (Lines[i] == 5):
#      break
  the_out = buff
  #the_out = Lines[len(Lines)-2]
#  print('---------')
#  print(Lines)
#  print('---------')
  ##the_out = Lines[len(Lines)-4]
  #the_out = Lines[len(Lines)-2]
  print(the_out)
except:
    exit(1)
