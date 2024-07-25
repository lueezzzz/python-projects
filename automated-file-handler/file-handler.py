import os
import sys
import time
import logging
from watchdog.observers import Observer


downloads = "/Users/RIAN/Downloads"
videos = "/Users/RIAN/Videos"
pictures = "/Users/Rian/Pictures"


class HandleDownloads():
    with os.scandir(pictures) as entries:
        for entry in entries:
            file_name = entry.name
            if file_name.endswith('.mp4') or file_name.endswith('.mov'):
                pass
            elif file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
                pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = downloads
    event_handler = HandleDownloads()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()