import configparser


class CONFIG:
    def __init__(self):
        """Configuration"""
        self._config = configparser.ConfigParser()
        self._config.read_file(open('config.cfg'))

        #####################################################
        #           I/O BENCHMARKS CONFIGURATION
        #####################################################
        self.FILE_SIZE = eval(self._config.get('DISK_BENCHMARK', 'FILE_SIZE'))
        self.FILE_AMOUNT = eval(self._config.get(
            'DISK_BENCHMARK', 'FILE_AMOUNT'))

        #####################################################
        #            CPU BENCHMARKS CONFIGURATION
        #####################################################
        self.CPU_BENCHMARK_JOB = int(
            self._config.get('CPU_BENCHMARK', 'CPU_BENCHMARK_JOB'))
        self.RD_NUM_SIZE = self._config.getint(
            'CPU_BENCHMARK', 'RD_NUM_SIZE')
        self.ARRAY_SIZE = self._config.getint('CPU_BENCHMARK', 'ARRAY_SIZE')

        ######################################################
        #            MEORY BENCHMARKS CONFIGURATION
        ######################################################
        self.MEMORY_BENCHMARK_JOB = self._config.getint(
            'MEMORY_BENCHMARK', "MEMORY_BENCHMARK_JOB")
