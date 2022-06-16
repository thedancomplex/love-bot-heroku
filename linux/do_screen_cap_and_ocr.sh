GetScreen()
{
	./get_screen.sh
	./do_crop.sh djap.png
	python3 do_process_img.py
}


GetScreen
IS_NEW=$(python3 get_img_diff.py)

echo -n $IS_NEW

if [ $IS_NEW -gt 0 ]
then
	./ocr_screen.sh
	#python3 read_jap.py
	sleep 2
	GetScreen
	cp djap.png.cropped djap.png.cropped.old
fi
