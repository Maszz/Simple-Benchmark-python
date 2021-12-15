import multiprocessing
import time
from timeConvert import TimeConverter as tc
import random
import numpy as np
import configparser


class Benchmark:
    def __init__(self):
        """
        Initialize worker and mulltiprocessing varable .
        ** In multiprocessor we can't get the returnValue in direct way, using manager in Multiprocess to get the output.

        """
        config = configparser.ConfigParser()
        config.read_file(open('config.cfg'))
        self.job = int(config.get('CPU_BENCHMARK', 'BENCHMARK_JOB'))
        self.rd_num_size = int(config.get('CPU_BENCHMARK', 'RD_NUM_SIZE'))
        self.arrays_size = int(config.get('CPU_BENCHMARK', 'ARRAY_SIZE'))
        self.results = []
        self.returnValue = dict()
        self.worker = multiprocessing.cpu_count()
        self.excuteTime = None

    def multicoreBenchmark(self):
        """
        Main algorithm to assigning job to process.
        Multiprocessing is module to create multiple of process intredsof one process.
        to efficiently using CPU, This function assigning job to process depends on CPU_COUNT
        assign process to every thread of cpu.
        :param : Job amount to assign to process .
        :return :None
        """
        start = time.time()
        process = list()
        iterations = self.job // self.worker
        fractionOfJob = self.job % self.worker
        # stressMemory = os.urandom(psutil.virtual_memory().total)

        for worker in range(self.worker):
            if fractionOfJob != 0:
                p = multiprocessing.Process(
                    target=self.benchmarkProcess, args=(self.returnValue, worker, iterations+1))
                fractionOfJob -= 1
                process.append(p)
                p.start()
            else:
                p = multiprocessing.Process(
                    target=self.benchmarkProcess, args=(self.returnValue, worker, iterations))
                process.append(p)
                p.start()
        for p in process:
            p.join()
        stop = time.time()
        self.excuteTime = tc(stop - start).toShortString()

    def benchmarkProcess(self, returnDict, workerNumber, iterations):
        """
        Process target function that comfortable form to :meth:`multicoreBenchmark` .
        This function calls :meth:`benchmark algorithm` .
        :param:returnDict, workerNumber, iteration to process algorithm.
        :return: None ,**using multiprocessing manager to get return Value.
        """
        temp = list()
        for _ in range(iterations):
            a = self.benchMarkAlgorithms()
            temp.append(a[0])

        returnDict[workerNumber] = temp

    def benchMarkAlgorithms(self, ):
        """
        Algorithm for benchmarking.
        """
        start = time.time()
        x = np.array([[random.getrandbits(self.rd_num_size) for _ in range(self.arrays_size)]
                      for _ in range(self.arrays_size)])

        y = np.array([[random.getrandbits(self.rd_num_size) for _ in range(self.arrays_size)]
                      for _ in range(self.arrays_size)])
        z = x@y
        stop = time.time()
        return (stop - start, z)


if __name__ == '__main__':
    a = Benchmark()
    a.multicoreBenchmark(50)
    print(a.excuteTime)
