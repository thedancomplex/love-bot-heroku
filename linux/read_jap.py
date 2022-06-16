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
  the_out = Lines[len(Lines)-4]
  #the_out = Lines[len(Lines)-2]
  print(the_out)
except:
    exit(1)
