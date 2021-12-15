import time
import os
import psutil
from timeConvert import TimeConverter as tc
from functools import lru_cache
import configparser


class MemoryBenchmark:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read_file(open('config.cfg'))
        self.job = int(config.get('MEMORY_BENCHMARK', 'MEMORY_BENCHMARK_JOB'))
        self.maxmemory = psutil.virtual_memory().total
        self.result = None

    # def memoryTest(self, n):
    #     """
    #     This func assign a byte size of total virtual memory .

    #     """
    #     # self.cache = dict()
    #     temp = os.urandom(self.maxmemory)
    #     start = time.time()
    #     for i in range(n):
    #         self.fibonacci_sequence(i)
    #     stop = time.time()
    #     # self.cache = None

        # return (tc(stop-start).toString())

    def memoryBenchmark(self):
        """
        Fibo level memorizing use LRU Cache
        """
        temp = os.urandom(self.maxmemory)
        start = time.time()
        for i in range(self.job):
            self.fibonacci_sequence(i)
        stop = time.time()
        # stat = self.fibonacci_sequence.cache_info()
        self.fibonacci_sequence.cache_clear()
        self.result = tc(stop-start).toShortString()

    @lru_cache(maxsize=128)
    def fibonacci_sequence(self, n):
        if n < 2:
            return 1
        else:
            return self.fibonacci_sequence(n-1)+self.fibonacci_sequence(n-2)


if __name__ == '__main__':
    a = MemoryBenchmark()
    print(a.memoryBenchmark(1000000))
