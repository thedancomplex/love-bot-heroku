./get_screen.sh
./do_crop.sh djap.png

IS_NEW=$(python3 get_img_diff.py)
if [ $IS_NEW -gt 0 ]
then
	./ocr_screen.sh
	python3 read_jap.py
	sleep 5
	./get_screen.sh
	./do_crop.sh djap.png
	cp djap.png.cropped djap.png.cropped.old
fi
