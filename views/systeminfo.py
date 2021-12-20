import platform
import socket
import re
import uuid
import json
import psutil
import logging
from tkinter import *
from views import Table as T


class SysteminfoFrame:
    def __init__(self, root):
        self.flm = Frame(master=root)
        self.info = self.getSystemInfo()
        lbl_platform = Label(
            master=self.flm, text=f"platform : {self.info['platform']}")

        lbl_architecture = Label(
            master=self.flm, text=f"architecture : {self.info['architecture']}")
        lbl_hostname = Label(
            master=self.flm, text=f"hostname : {self.info['hostname']}")
        lbl_mac_address = Label(
            master=self.flm, text=f"mac-address : {self.info['mac-address']}")
        lbl_processor = Label(
            master=self.flm, text=f"processor : {self.info['processor']}")
        lbl_ram = Label(master=self.flm, text=f"ram : {self.info['ram']}")

        lbl_platform.grid(row=0, column=0)
        lbl_architecture.grid(row=1, column=0)
        lbl_hostname.grid(row=2, column=0)
        lbl_mac_address.grid(row=3, column=0)
        lbl_processor.grid(row=4, column=0)
        lbl_ram.grid(row=5, column=0)

    def getSystemInfo(self):
        try:
            info = dict()
            info['platform'] = platform.system()
            info['platform-release'] = platform.release()
            info['platform-version'] = platform.version()
            info['architecture'] = platform.machine()
            info['hostname'] = socket.gethostname()
            info['mac-address'] = ':'.join(re.findall('..',
                                                      '%012x' % uuid.getnode()))
            info['processor'] = platform.processor()
            info['ram'] = str(
                round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
            return info
        except Exception as e:
            logging.exception(e)
