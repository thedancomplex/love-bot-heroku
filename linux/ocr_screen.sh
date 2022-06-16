cp djap.png.cropped djap.png.cropped.png
convert -resize 300% djap.png.cropped.png djap.png.cropped.300.png
tesseract djap.png.cropped.300.png  jap_ocr -l jpn
#THE_WORDS=$(< jap_ocr.txt)
THE_WORDS=$(python3 read_jap.py)
echo '----------'
echo '----------'
echo '----------'
echo $THE_WORDS
echo '----------'
echo '----------'
echo '----------'
#sleep 5
python3 do_type.py $THE_WORDS
cat jap_ocr.txt
