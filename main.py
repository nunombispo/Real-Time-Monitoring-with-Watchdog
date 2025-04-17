from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_created(self, event):
        print(f"Created: {event.src_path}")
        

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

# Replace with the path I want to monitor
path = "dir_path"
handler = MyHandler()
observer = Observer()
observer.schedule(handler, path=path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()