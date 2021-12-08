import os
import math
import time
import random
import shutil
import sys
from timeConvert import TimeConverter as tc
import psutil


class HarddiskBenchmark:
    def __init__(self, filename=None):
        self.filename = filename
        try:
            os.mkdir("temp")
        except FileExistsError:
            self.deleteTempFile()

        # os.mkdir("temp2")

        self.fileSize = 1024*128*2
        self.fileAmount = 8000*2*2
        # self.createFiles(self.fileAmount, self.fileSize)
        self.createFilesOs(self.fileAmount, self.fileSize)

        # self.sequentialRead(self.fileAmount,)
        self.sequentialRead_os(self.fileAmount, self.fileSize)
        # self.sequentialWrite(self.fileAmount, self.fileSize)
        self.sequentialWrite_os(self.fileAmount, self.fileSize)

        # self.randomRead()
        # self.sequentialWrite2()
        # self.randomRead2()

        """Generator for output"""
        # created = self.createFiles(self.fileSize)
        # for i in created:
        #     print(i)
        # sequentialRead = self.sequentialRead()
        # for i in sequentialRead:
        #     print(i)
        # for i in self.randomRead():
        #     print(i)

        self.deleteTempFile()

    def createFiles(self, fileAmount, size):
        """
        createdFile benchmark created binary file for {fileAmont} times @ size {size} bytes.
        In development don't open directory.
        :param : Integer of size in bytes.
        :return : None.
        """
        # yield 'start'
        start = time.time()

        for i in range(fileAmount):
            with open(f"temp/{i}.dat", 'wb') as binaryfile:
                binaryfile.write(os.urandom(size))
        stop = time.time() - start
        # yield f'finish in {stop}'
        print(f'Created time: {tc(stop).toString()}')

    def createFilesOs(self, fileAmount, size):
        """
        createdFile benchmark created binary file for 300000times @ size 1024 bytes.
        In development don't open directory.
        :param : Integer of binary size in bytes.
        :return : None.
        """
        # yield 'start'
        start = time.time()

        for i in range(fileAmount):
            # with open(f"temp/{i}.dat", 'wb') as binaryfile:
            #     binaryfile.write(os.urandom(size))
            f = os.open(f"temp/{i}.dat", os.O_CREAT | os.O_WRONLY, 0o777)
            os.write(f, os.urandom(size))
            os.fsync(f)

            os.close(f)
        stop = time.time() - start
        # yield f'finish in {stop}'
        print(f'Created time: {tc(stop).toString()}')

    def sequentialRead(self, fileAmount):
        start = time.time()
        # yield 'start'

        for i in range(fileAmount):
            with open(f"temp/{i}.dat", "rb") as f:
                f.seek(0)
                f.read()
                # with open(os.devnull, "wb") as devnull:
                #     devnull.write(f.read())

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

    def sequentialRead_os(self, fileAmount, fileSize):
        start = time.time()
        for i in range(fileAmount):
            # print(i)
            f = os.open(f"temp/{i}.dat", os.O_RDONLY)
            os.lseek(f, 0, os.SEEK_SET)
            os.read(f, fileSize)
            os.close(f)

        print(f'sequentialread os time: {tc(time.time()-start).toString()}')

    def sequentialWrite_os(self, fileAmount, fileSize):
        start = time.time()
        for i in range(fileAmount):
            f = os.open(f"temp/{i}.dat", os.O_CREAT | os.O_WRONLY, 0o777)

            buff = os.urandom(fileSize)
            os.write(f, buff)
            os.fsync(f)
            # stop = time.time() - start1
            os.close(f)
        print(f'sequentialWriteOs time: {tc(time.time()-start).toString()}')

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
        start = time.time()
        shutil.rmtree("temp")

        stop = time.time()
        print(f'delete temp {tc(stop-start).toString()}')
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
