import os
import time
import threading
import webbrowser
import pytesseract
import urllib.parse
from PIL import ImageGrab
from infi.systray import SysTrayIcon

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

paused = True

exit_flag = False

def start(systray):
    global paused
    paused = False

def pause(systray):
    global paused
    paused = True

def exit(systray):
    global exit_flag
    exit_flag = True

menu_options = (("Start", None, start),
                ("Pause", None, pause),
                ("Exit", None, exit))

def main():
    systray = SysTrayIcon(resource_path("qs.ico"), "quickscope 1.0", menu_options)
    systray.start()

    thread = threading.Thread(target=main_loop)
    thread.start()

    thread.join()

    systray.shutdown()

def main_loop():
    global paused
    global exit_flag
	
    last_image_data = None
    last_text = None

    while not exit_flag:
        if not paused:
            image_data = ImageGrab.grabclipboard()

            if image_data is not None and image_data != last_image_data:
                rd = pytesseract.image_to_string(image_data, lang='eng')

                if rd and rd != last_text:
                    encoded_rd = urllib.parse.quote(rd)
                    webbrowser.open_new_tab(f'https://www.google.com/search?q={encoded_rd}')

                last_image_data = image_data
                last_text = rd
        
        time.sleep(1)

if __name__ == '__main__':
    main()
