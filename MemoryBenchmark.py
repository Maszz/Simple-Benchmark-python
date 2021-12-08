import time
import os
import psutil
# from timeConvert import TimeConverter as tc


class MemoryBenchmark:
    def __init__(self):
        self.maxmemory = psutil.virtual_memory().total
        self.memoryStressTest()

    def memoryStressTest(self):
        """
        This func assign a byte size of total virtual memory .

        """
        start = time.time()
        temp = os.urandom(8589934592)
        stop = time.time()

        print(stop-start)
        # temp.hex()
        # print((self.maxmemory/(1024*1024))/(stop-start))
        # print(stop-start)
        # print(psutil.virtual_memory())
        # time.sleep(30)


if __name__ == '__main__':
    a = MemoryBenchmark()
    # print(psutil.virtual_memory().total/8)
