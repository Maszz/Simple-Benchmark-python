import os
import math
import time
import random
import shutil
import sys
from timeConvert import TimeConverter as tc
import psutil
import configparser


class HarddiskBenchmark:
    def __init__(self):
        """
        Initialize HarddiskBenchmark object. 
        try to create temporary directory if it doesn't exist
        setting up config for benchmark [filesize] , [fileAmount]
        :param : 

        """
        config = configparser.ConfigParser()
        config.read_file(open('config.cfg'))
        self.fileSize = eval(config.get('I/O_BENCHMARK', 'FILE_SIZE'))
        self.fileAmount = eval(config.get('I/O_BENCHMARK', 'FILE_AMOUNT'))
        self.result = list()
        try:
            os.mkdir("temp")
        except FileExistsError:
            self.deleteTempFile()
            os.mkdir("temp")

        # self.createFiles(self.fileAmount, self.fileSize)
        # self.createFilesOs(self.fileAmount, self.fileSize)

        # self.sequentialRead(self.fileAmount,)
        # self.sequentialRead_os(
        #     self.fileAmount, self.fileSize)
        # self.sequentialWrite(self.fileAmount, self.fileSize)
        # self.sequentialWrite_os(
        #     self.fileAmount, self.fileSize)

        # self.deleteTempFile()

    def createFiles(self, fileAmount, size):
        """
        createdFile benchmark created binary file for {fileAmont} times @ size {size} bytes.
        In development don't open directory.
        :param : Integer of size in bytes.
        :return : None.
        """
        # yield 'start'
        start = time.time()

        for i in range(self.fileAmount):
            with open(f"temp/{i}.dat", 'wb') as binaryfile:
                binaryfile.write(os.urandom(self.fileSize))
        stop = time.time() - start
        # yield f'finish in {stop}'
        return tc(stop).toString()

    def createFilesOs(self):
        """
        createdFile benchmark created binary file for 300000times @ size 1024 bytes.
        In development don't open directory.
        :param : Integer of binary size in bytes.
        :return : None.
        """
        # yield 'start'
        start = time.time()

        for i in range(self.fileAmount):
            # with open(f"temp/{i}.dat", 'wb') as binaryfile:
            #     binaryfile.write(os.urandom(size))
            f = os.open(f"temp/{i}.dat", os.O_CREAT | os.O_WRONLY, 0o777)
            os.write(f, os.urandom(self.fileSize))
            os.fsync(f)

            os.close(f)
        stop = time.time() - start
        # yield f'finish in {stop}'
        self.result.append(tc(stop).toShortString())

    def sequentialRead(self, fileAmount):
        start = time.time()
        # yield 'start'

        for i in range(fileAmount):
            with open(f"temp/{i}.dat", "rb") as f:
                f.seek(0)
                f.read()

        # yield f'finish in {stop}'
        print(f'sequentialRead time: {tc(time.time() - start).toString()}')
        # print(f'sequentialRead speed: {(30000*1024)/sum(r_times)}')

    def sequentialWrite(self, fileAmount, fileSize,):
        start = time.time()
        # yield 'start'

        for i in range(fileAmount):
            with open(f"temp/{i}.dat", "wb") as f:
                f.seek(0)
                f.write(os.urandom(fileSize))

        stop = time.time() - start
        # yield f'finish in {stop}'
        print(f'sequentialWrite time: {tc(stop).toString()}')

    def sequentialRead_os(self):
        start = time.time()
        for i in range(self.fileAmount):
            # print(i)
            f = os.open(f"temp/{i}.dat", os.O_RDONLY)
            os.lseek(f, 0, os.SEEK_SET)
            os.read(f, self.fileSize)
            os.close(f)
        stop = time.time() - start

        self.result.append(tc(stop).toShortString())

    def sequentialWrite_os(self):
        start = time.time()
        for i in range(self.fileAmount):
            f = os.open(f"temp/{i}.dat", os.O_CREAT | os.O_WRONLY, 0o777)

            buff = os.urandom(self.fileSize)
            os.write(f, buff)
            os.fsync(f)
            # stop = time.time() - start1
            os.close(f)
        stop = time.time() - start
        self.result.append(tc(stop).toShortString())

    # def randomRead(self):
    #     start = time.time()
    #     # yield 'start'

    #     for i in range(100000):
    #         with open(f"temp/{math.floor(random.random()*10000)}.dat", "rb") as f:
    #             f.seek(random.randint(0, 1024))
    #             f.read()

    #             # file.read()
    #             # with open(os.devnull, "wb") as devnull:
    #             #     devnull.write(f.read())
    #     stop = time.time() - start
    #     # yield f'finish in {stop}'

    #     print(f'randomRead time: {tc(stop).toString()}')

    def deleteTempFile(self):
        """
        Delete temporary directory for benchmarking.
        """
        start = time.time()
        shutil.rmtree("temp")

        stop = time.time() - start
        self.result.append(tc(stop).toShortString())
        # start = time.time()

        # shutil.rmtree("temp2")
        # stop = time.time()

        # print(f'delete temp2 {tc(stop-start).toString()}')

    # def sequentialWrite2(self):
    #     start = time.time()
    #     # yield 'start'
    #     w_times = []
    #     f = os.open("temp///test", os.O_CREAT | os.O_WRONLY, 0o777)
    #     for i in range(1000):

    #         buff = os.urandom(1024*1024)
    #         start1 = time.time()
    #         os.write(f, buff)
    #         os.fsync(f)
    #         w_times.append(time.time()-start1)
    #         # stop = time.time() - start1
    #     os.close(f)
    #     write_speed = 128/sum(w_times)

    #     # yield f'finish in {stop}'
    #     print(f'sequentialWrite time: {tc(time.time()-start).toString()}')
    #     print(f'sequentialWrite speed: {write_speed}')

    # def randomRead2(self):
    #     f = os.open("temp///test", os.O_RDONLY, 0o777)
    #     # Generate Random Read Positions
    #     offsets = list(range(0, 128 * 1024*1024, 1024*1024))
    #     random.shuffle(offsets)
    #     start = time.time()

    #     r_times = []
    #     for o in offsets:
    #         start1 = time.time()
    #         os.lseek(f, o, os.SEEK_SET)  # Set Position
    #         buff = os.read(f, 1024*1024)  # Read From Position
    #         t = time.time() - start1
    #         if not buff:
    #             break  # If EOF Reached
    #         r_times.append(t)
    #     os.close(f)

    #     read_speed = 128/sum(r_times)  # MB/s
    #     print(f'sequentialwrite time: {tc(start-time.time()).toString()}')
    #     print(f'sequentialwrite speed: {read_speed}')


if __name__ == "__main__":
    a = HarddiskBenchmark()
    # b = os.urandom(psutil.virtual_memory().total)
    # print(b)
