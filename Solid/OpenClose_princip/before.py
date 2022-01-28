import sys
import time

preambula = ''' 
                Есть класс логгер, котрый выводит строку в формате
                '%Y-%b-%d %H:%M:%S'. Требуется модтифицировать формат вывода.
                Следуя принципу OCP - модифицировать нельзя,
                поэтому будем расширять. Наследуем класс и переопределим
                формат вывода. Вообще лучше создать базовый класс Logger и 
                наследоваться уже от него.
                '''

class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message):
        sys.stderr.write(f'{self.prefix} --> {message}\n')

print(preambula)
print("Cмотри файл after.py")