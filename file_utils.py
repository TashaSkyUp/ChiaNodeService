import random
import threading
import time
import shutil
import subprocess
import sys
import os

counter = 0


class progress_file_move:
    def __init__(self, source: str, dest: str):
        self.source = source
        self.dest = dest
        self.mydir = "/".join(sys.argv[0].split("/")[:-1])
        self.file_size = self.get_source_file_size()
        print(self.mydir)
        t = threading.Thread(target=self.worker)
        t.start()
        size = 0

        while size < self.file_size:
            size = self.get_dest_file_size()
            percent = str(size / self.file_size)
            print('\b' * 100 + str(size) + "/" + str(self.file_size) + " = " + percent + '%', end='')
            time.sleep(.001)

    def worker(self):
        shutil.move(self.source, self.dest)
        return

    def get_worker_state(self):
        df = subprocess.Popen(["cat", self.mydir + "/tmp.tmp"],
                              stdout=subprocess.PIPE)
        output = df.communicate()[0]
        output = output.decode("utf8")
        return output

    def get_source_file_size(self):
        try:
            size = os.path.getsize(self.source)
        except FileNotFoundError:
            return 0
        return size

    def get_dest_file_size(self):
        try:
            size = os.path.getsize(self.dest)
        except FileNotFoundError:
            return 0
        return size


def test():
    filemove = progress_file_move("/swapfile", "/swapfile2")
