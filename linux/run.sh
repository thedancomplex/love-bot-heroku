./do_start.sh
while [ 1 -eq 1 ]
do
	python3 do_move_mouse.py
	./do_screen_cap_and_ocr.sh
	sleep 60
done
