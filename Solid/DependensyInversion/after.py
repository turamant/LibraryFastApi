import sys
import time


class PrinterTerminal:
    def write(self, msg):
        sys.stderr.write(f'{msg}\n')

class PrinterFile:
    def write(self, msg):
        with open('out_after.txt', 'w', encoding='UTF8') as f:
            f.write(f'{msg}\n')

class Logger:
    def __init__(self):
        self.prefix = time.strftime("%Y-%b-%d", time.localtime())

    def writer(self, message, notifyer):
        notifyer().write(f'{self.prefix} {message}')

log = Logger()
log.writer("Gello ammigas in printer", PrinterFile)
log.writer("Hello amigo in terminal!", PrinterTerminal)