import keyboard
import time

last_time = None

def on_key_event(event):
    global last_time
    if event.event_type != "down":
        return
    now = time.time()
    if last_time is None:
        diff = 0.0
    else:
        diff = now - last_time
    last_time = now
    print(f"Key: {event.name:<10}  Interval: {diff:.3f} sec")

def main():
    print("=== キー入力キャッチ開始 ===")
    print("終了するには ESC を押してください\n")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')
    print("=== 終了しました ===")

if __name__ == "__main__":
    main()
