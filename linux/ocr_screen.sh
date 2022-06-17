BOT_NAME_ELENA='Hikari'
BOT_NAME_DAN='Love-Bot'
CONVERSATION_FILE='conversation'
CONVERSATION_FILE_ENGLISH=$CONVERSATION_FILE.english

cp djap.png.cropped djap.png.cropped.png
convert -resize 300% djap.png.cropped.png djap.png.cropped.300.png
tesseract djap.png.cropped.300.png  jap_ocr -l jpn >/dev/null 2>&1
#tesseract djap.png.cropped.300.png  jap_ocr -l jpn
#THE_WORDS=$(< jap_ocr.txt)
TIME1=$(date)
THE_WORDS_READ=$(python3 read_jap.py)
THE_WORDS_READ_SCORE=$(python3 do_translate_and_score.py $THE_WORDS_READ)
THE_WORDS_READ_ENGLISH=$(python3 do_translate.py $THE_WORDS_READ)

THE_FILE=$CONVERSATION_FILE.log
echo -n $BOT_NAME_ELENA >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $TIME1 >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $THE_WORDS_READ_SCORE >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo $THE_WORDS_READ >> $THE_FILE


THE_FILE=$CONVERSATION_FILE_ENGLISH.log
echo -n $BOT_NAME_ELENA >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $TIME1 >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $THE_WORDS_READ_SCORE >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo $THE_WORDS_READ_ENGLISH >> $THE_FILE



THE_WORDS_REPLY=$(python3 do_response.py $THE_WORDS_READ)
THE_WORDS_REPLY_SCORE=$(python3 do_translate_and_score.py $THE_WORDS_REPLY)
THE_WORDS_REPLY_ENGLISH=$(python3 do_translate.py $THE_WORDS_REPLY)


TIME1=$(date)
THE_FILE=$CONVERSATION_FILE.log
echo -n $BOT_NAME_DAN >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $TIME1 >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $THE_WORDS_REPLY_SCORE >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo $THE_WORDS_REPLY >> $THE_FILE


THE_FILE=$CONVERSATION_FILE_ENGLISH.log
echo -n $BOT_NAME_DAN >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $TIME1 >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo -n $THE_WORDS_REPLY_SCORE >> $THE_FILE
echo -n ' : ' >> $THE_FILE
echo $THE_WORDS_REPLY_ENGLISH >> $THE_FILE



echo ' '
echo '----------'
echo '---Read---'
echo '----------'
echo $THE_WORDS_READ
echo $THE_WORDS_READ_ENGLISH
echo $THE_WORDS_READ_SCORE
echo '----------'
echo '----------'
echo '----------------'
echo '----------'
echo '---Reply--'
echo '----------'
echo $THE_WORDS_REPLY
echo $THE_WORDS_REPLY_ENGLISH
echo $THE_WORDS_REPLY_SCORE
echo '----------'
echo '----------'
echo '----------'
echo '########################'
#sleep 5
python3 do_type.py $THE_WORDS_REPLY
#cat jap_ocr.txt
