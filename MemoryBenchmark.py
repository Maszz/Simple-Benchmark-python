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

    def memoryStressTest(self, n):
        """
        This func assign a byte size of total virtual memory .

        """
        temp = os.urandom(self.maxmemory)
        start = time.time()
        for i in range(n):
            self.fibonacci_sequence_memorizing(i)
        stop = time.time()

        return (tc(stop-start).toString())

    def cacheMemory(self, n):
        """
        Fibo level memorizing use LRU Cache
        """
        start = time.time()
        for i in range(n):
            # self.fibonacci_sequence(i)
            self.fibonacci_sequence(i)
        stop = time.time()
        stat = self.fibonacci_sequence.cache_info()
        self.fibonacci_sequence.cache_clear()
        return stop-start, stat

    @lru_cache(maxsize=128)
    def fibonacci_sequence(self, n):
        if n < 2:
            return 1
        else:
            return self.fibonacci_sequence(n-1)+self.fibonacci_sequence(n-2)

    @lru_cache(maxsize=0)
    def fibonacci_sequence_memorizing(self, n):
        if n in self.cache:
            return self.cache[n]
        elif n < 2:
            self.cache[n] = 1
            return self.cache[n]
        else:
            self.cache[n] = self.fibonacci_sequence_memorizing(
                n-1)+self.fibonacci_sequence_memorizing(n-2)
            return self.cache[n]


if __name__ == '__main__':
    a = MemoryBenchmark()
    print(a.memoryStressTest(100000))
