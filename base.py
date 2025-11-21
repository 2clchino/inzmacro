import time
import threading
import pyautogui
import keyboard

START_HOTKEY = "F8"
STOP_HOTKEY = "F9"
LOOP_INTERVAL = 0.5
running = False

# ==============================

def do_macro_actions():
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    time.sleep(11)
    pyautogui.press("a")
    time.sleep(4)
    pyautogui.press("s")
    
    time.sleep(11)
    pyautogui.press("a")
    time.sleep(4)
    pyautogui.press("s")
    
    time.sleep(11)
    pyautogui.press("a")
    time.sleep(4)
    pyautogui.press("s")
    time.sleep(12)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(63)

def macro_loop():
    global running
    print("[INFO] マクロ開始")

    while running:
        start = time.time()
        do_macro_actions()
        elapsed = time.time() - start
        wait = max(0, LOOP_INTERVAL - elapsed)
        time.sleep(wait)

def start_macro():
    global running
    if running:
        print("[INFO] すでに実行中です")
        return
    running = True
    thread = threading.Thread(target=macro_loop, daemon=True)
    thread.start()


def stop_macro():
    global running
    if not running:
        print("[INFO] マクロは動作していません")
        return
    running = False
    print("[INFO] マクロ終了")


def main():
    pyautogui.FAILSAFE = True
    print("========== キーボードマクロ ==========")
    print(f"{START_HOTKEY} で開始, {STOP_HOTKEY} で停止")
    print("Ctrl+C でスクリプト終了")
    print("======================================")

    keyboard.add_hotkey(START_HOTKEY, start_macro)
    keyboard.add_hotkey(STOP_HOTKEY, stop_macro)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] 終了します")
        stop_macro()


if __name__ == "__main__":
    main()
