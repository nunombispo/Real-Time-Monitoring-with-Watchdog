import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FilteredHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            logging.info(f"Modified .txt file: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            logging.info(f"Created .txt file: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            logging.info(f"Deleted .txt file: {event.src_path}")

def monitor_path(path, recursive=False):
    handler = FilteredHandler()
    observer = Observer()
    observer.schedule(handler, path=path, recursive=recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# For example, I monitor a directory for .txt files
monitor_path("dir_path", recursive=True)