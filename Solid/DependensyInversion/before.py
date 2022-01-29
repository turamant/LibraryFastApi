import sys
import time


class PrinterTerminal:
    def write(self, msg):
        sys.stderr.write(f'{msg}\n')

class PrinterFile:
    def write(self, msg):
        with open('out_before.txt', 'a+', encoding='UTF8') as f:
            f.write(f'{msg}\n')

class Logger:
    def __init__(self):
        self.prefix = time.strftime("%Y-%b-%d", time.localtime())

    def log_stderr(self, message):
        PrinterTerminal().write(f'{self.prefix} {message}')

    def log_file(self, message):
        PrinterFile().write(f'{self.prefix} {message}')

log = Logger()
log.log_stderr("Gello ammigas")
log.log_file("Ket na kutak")