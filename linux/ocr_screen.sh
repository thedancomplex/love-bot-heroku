tesseract djap.png  jap_ocr -l jpn
THE_WORDS=$(< jap_ocr.txt)
echo "waiting 5 sec to pring"
echo $THE_WORDS
sleep 5
python3 do_type.py $THE_WORDS
cat jap_ocr.txt
