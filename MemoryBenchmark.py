import time
import os
import psutil
from timeConvert import TimeConverter as tc
from functools import lru_cache


class MemoryBenchmark:
    def __init__(self):
        self.maxmemory = psutil.virtual_memory().total
        # self.memoryStressTest()
        self.cache = dict()

    def memoryStressTest(self):
        """
        This func assign a byte size of total virtual memory .

        """
        start = time.time()
        temp = os.urandom(8589934592)
        stop = time.time()

        print(tc(stop-start).toString())
        # temp.hex()
        # print((self.maxmemory/(1024*1024))/(stop-start))
        # print(stop-start)
        # print(psutil.virtual_memory())
        # time.sleep(30)

    def cacheMemory(self, n):
        """
        Fibo level memorizing use LRU Cache
        """
        start = time.time()
        for i in range(n):
            # self.fibonacci_sequence(i)
            self.fibo_dynamic_cache(i)
        stop = time.time()
        return stop-start, self.fibonacci_sequence.cache_info()

    @lru_cache(maxsize=128)
    def fibonacci_sequence(self, n):
        if n <= 2:
            return 1
        else:
            return self.fibonacci_sequence(n-1)+self.fibonacci_sequence(n-2)


if __name__ == '__main__':
    a = MemoryBenchmark()

    print(a.cacheMemory(1000000))
    # print(a.fibo_dynamic_cache(10))
    # print(psutil.virtual_memory().total/8)
