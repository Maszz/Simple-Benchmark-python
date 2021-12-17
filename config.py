import configparser
import platform


class Config:
    def __init__(self):
        """Configuration"""
        self._config = configparser.ConfigParser()
        self.checkSystem()
        self.WIDTH = self._config.get('TABLE', 'WIDTH')
        self.fontsize = self._config.getint('TABLE', 'FONT_SIZE')
        self.fileSize = self._config.getint('I/O_BENCHMARK', 'FILE_SIZE')
        self.fileAmount = eval(self._config.get(
            'I/O_BENCHMARK', 'FILE_AMOUNT'))

    def checkSystem(self):
        if(platform.system() == "Darwin"):

            self._config.read_file(open('config.cfg'))
        if platform.system() == "Windows":
            self._config.read_file(open('config.cfg'))
