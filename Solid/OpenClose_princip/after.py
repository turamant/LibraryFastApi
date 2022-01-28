import sys
import time

preambula = '''
                Есть класс логгер, котрый выводит строку в формате
                '%Y-%b-%d %H:%M:%S'. Требуется модтифицировать формат вывода.
                Следуя принципу OCP - модифицировать нельзя,
                поэтому будем расширять. Наследуем класс и переопределим
                формат вывода.
                Вообще лучше создать базовый класс Logger и наследоваться уже 
                от него.
            '''

class LoggerBase:
    def __init__(self):
        self.prefix = ''

    def log(self, message):
        sys.stderr.write(f'{self.prefix} --> {message}\n')

class Logger(LoggerBase):
    """ расширяем , но не модифицируем"""
    def __init__(self):
        super(LoggerBase, self).__init__()
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

class LoogerExtension(LoggerBase):
    """ расширяем , но не модифицируем"""
    def __init__(self):
        super(LoogerExtension, self).__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())


print(preambula)
log = Logger()
log.log('произошла ошибка!')

log_ext = LoogerExtension()
log_ext.log('error has happened!')


