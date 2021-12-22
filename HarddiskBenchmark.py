import os
import time
import shutil

from config import *


class HarddiskBenchmark:
    def __init__(self):
        """
        Initialize HarddiskBenchmark object. 
        try to create temporary directory if it doesn't exist
        setting up config for benchmark `filesize` , `fileAmount`


        """
        config = CONFIG()
        self.fileSize = config.FILE_SIZE
        self.fileAmount = config.FILE_AMOUNT
        self.result = list()
        self.benchmarkTime = None

        # try create temp directory
        try:
            os.mkdir("temp")
        except FileExistsError:
            self.deleteTempFile()
            os.mkdir("temp")

    def startBenchmark(self):
        start = time.time()
        self.createFilesBench()
        self.writeFileBench()
        self.readFilesBench()
        self.deleteTempFile()
        stop = time.time() - start

        self.benchmarkTime = stop

    def createFilesBench(self):
        """
        createdFile benchmark created binary file for `self.fileAmount` @ size `self.fileSize` bytes.
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
        """
        read file that created from :meth :`self.createFilesBench`
        :param : None
        :return : None
        """
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
        """
        appending byte to file creatd by :meth :`createFilesBench`
        """
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
    a.startBenchmark()
    print(a.benchmarkTime)
    print(sum(a.result))
