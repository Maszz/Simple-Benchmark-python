import os
import math
import time
import random
import shutil
import sys
from timeConvert import TimeConverter as tc
import psutil
import configparser
from config import *


class HarddiskBenchmark:
    def __init__(self):
        """
        Initialize HarddiskBenchmark object. 
        try to create temporary directory if it doesn't exist
        setting up config for benchmark `filesize` , `fileAmount`
        :param : 

        """
        config = CONFIG()
        self.fileSize = config.FILE_SIZE
        self.fileAmount = config.FILE_AMOUNT
        self.result = list()
        try:
            os.mkdir("temp")
        except FileExistsError:
            self.deleteTempFile()
            os.mkdir("temp")

    def createFilesBench(self):
        """
        createdFile benchmark created binary file for `self.fileAmount` @ size `self.fileSize` bytes.
        In development don't open directory.
        :param : None
        :return : None.
        """
        start = time.time()

        for i in range(self.fileAmount):

            f = os.open(f"temp/{i}.dat", os.O_CREAT, 0o777)

            os.close(f)
        stop = time.time() - start
        self.result.append(stop)

    def readFilesBench(self):
        start = time.time()
        for i in range(self.fileAmount):
            # print(i)
            f = os.open(f"temp/{i}.dat", os.O_RDONLY, 0o777)
            os.lseek(f, 0, os.SEEK_SET)
            os.read(f, self.fileSize)
            os.close(f)
        stop = time.time() - start

        self.result.append(stop)

    def writeFileBench(self):
        start = time.time()
        for i in range(self.fileAmount):
            f = os.open(f"temp/{i}.dat", os.O_APPEND | os.O_WRONLY, 0o777)

            buff = os.urandom(self.fileSize)
            os.write(f, buff)
            os.fsync(f)
            os.close(f)
        stop = time.time() - start
        self.result.append(stop)

    def deleteTempFile(self):
        """
        Delete temporary directory for benchmarking.
        """
        start = time.time()
        shutil.rmtree("temp")

        stop = time.time() - start
        self.result.append(stop)


if __name__ == "__main__":
    a = HarddiskBenchmark()

    # b = os.urandom(psutil.virtual_memory().total)
    # print(b)
