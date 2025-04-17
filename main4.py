from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
from threading import Timer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DebouncedHandler(FileSystemEventHandler):
    def __init__(self):
        self.timer = None

    def on_any_event(self, event):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(1.0, self.handle_event, args=[event])
        self.timer.start()

    def handle_event(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            logging.info(f"Event: {event.event_type} on {event.src_path}")

def monitor_path_with_debounce(path, recursive=False):
    handler = DebouncedHandler()
    observer = Observer()
    observer.schedule(handler, path=path, recursive=recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

monitor_path_with_debounce("dir_path", recursive=True)