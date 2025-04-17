from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"{event.event_type}: {event.src_path}")

def monitor_directories(directories):
    handler = MyHandler()
    observer = Observer()
    for directory in directories:
        observer.schedule(handler, path=directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

directories_to_monitor = ["dir_path", "dir_path2"]
monitor_directories(directories_to_monitor)