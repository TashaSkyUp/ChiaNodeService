import random
import threading
import time
import shutil
import subprocess
import sys
import os
import time
counter = 0


class progress_file_move:
    def __init__(self, source: str, dest: str):
        self.source = source
        self.dest = dest
        self.mydir = "/".join(sys.argv[0].split("/")[:-1])
        self.file_size = self.get_source_file_size()
        self.start_time = time.monotonic()
        self.time_elapsed = lambda: time.monotonic() - self.start_time
        self.error = ""
        #print(self.mydir)
        t = threading.Thread(target=self.worker)
        t.start()
        size = 0

        while (size < self.file_size)&(self.error==""):
            lsize = size
            size = self.get_dest_file_size()

            rate = size/(1024*1024)/self.time_elapsed()

            rate = str("{:.2f}".format(rate))

            percent = str((size / self.file_size)*100)
            percent = percent.split(".")
            percent[1] = percent[1][:2]
            percent = ".".join(percent)
            print('\b' * 100 + str(size) + "/" + str(self.file_size) + " = " + percent + '%', rate+" Mib/Sec",end='    ')
            time.sleep(0.01)
        t.join()
    def worker(self):
        try:
            shutil.move(self.source, self.dest)
        except shutil.SameFileError as err:
            self.error = err
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
