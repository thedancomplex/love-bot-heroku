GetScreen()
{
        ./get_screen.sh
        ./do_crop.sh djap.png
        python3 do_process_img.py
}

GetScreen
cp djap.png.cropped djap.png.cropped.old

