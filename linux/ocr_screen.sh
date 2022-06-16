cp djap.png.cropped djap.png.cropped.png
convert -resize 300% djap.png.cropped.png djap.png.cropped.300.png
tesseract djap.png.cropped.300.png  jap_ocr -l jpn
#THE_WORDS=$(< jap_ocr.txt)
THE_WORDS_READ=$(python3 read_jap.py)
THE_WORDS_REPLY=$(python3 do_response.py $THE_WORDS_READ)
echo '----------'
echo '---Read---'
echo '----------'
echo $THE_WORDS_READ
echo '----------'
echo '----------'
echo '----------'
echo '----------'
echo '---Reply--'
echo '----------'
echo $THE_WORDS_REPLY
echo '----------'
echo '----------'
echo '----------'
#sleep 5
python3 do_type.py $THE_WORDS_REPLY
cat jap_ocr.txt
