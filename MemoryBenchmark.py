import time
import os
import psutil
from timeConvert import TimeConverter as tc
from functools import lru_cache
from config import CONFIG


class MemoryBenchmark:
    """
    Memory Benchmark Class : This is Memmory benchmark using memorizing to implement 
    Benchmark 
    """

    def __init__(self):
        config = CONFIG()
        self.job = config.MEMORY_BENCHMARK_JOB
        self.MAX_MEMORY = psutil.virtual_memory().total
        self.result = None

    def memoryBenchmark(self):
        """
        This function calculates fibonacci sequence from :meth: `fibonacci_sequence` when memory is stressing.
        :param :None
        :return : None , store excuteTime to `self.result`
        """
        temp = os.urandom(self.MAX_MEMORY)
        start = time.time()
        for i in range(self.job):
            self.fibonacci_sequence(i)
        stop = time.time()
        self.fibonacci_sequence.cache_clear()
        self.result = stop-start

    @lru_cache(maxsize=128)
    def fibonacci_sequence(self, n):
        """
        This function calculates the fibonacci sequence using LRU caching
        :param n: term of fibonacci sequences
        :return: nth of fibonacci sequence 
        """
        if n < 2:
            return 1
        else:
            return self.fibonacci_sequence(n-1)+self.fibonacci_sequence(n-2)


if __name__ == '__main__':
    a = MemoryBenchmark()
    print(a.memoryBenchmark(1000000))
