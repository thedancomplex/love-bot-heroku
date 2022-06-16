# Love Bot

Love Bot will read a screen using OCR, decode it from japanese and reply in japanese.  It will automatically type the response in what ever active window is present.

## Getting started

Love Bot require multiple libraries including:
- Google Translate
- convert
- pyautogui
- codecs
- tesseract with japanese "jpn" ocr 
- gnome-screenshot

The system was tested on Ubuntu 20.04 with a screen resolution of 1920x1080 (1080p).  the image read is the bottom right hand of the screen.  This can be modified in the do_crop.sh file.

## Running
```
$ cd linux
$ ./run.sh
```

