preambula = '''
            Один класс выполняет два метода(ответственности)Б
            требуется разделить ответстевноость .
            Разделили класс на два:
            - Formatdata подготтавливает данные,
            - FileWriter другой выводит в файл
            '''


data = [
    {
        'name': 'Шерлок',
        'surname': 'Холмс',
        'occupation': 'частный детектив'
    },
    {
        'name': 'Джон',
        'surname': 'Ватсон',
        'occupation': 'доктор'
    }
]

class FormatData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):
        result = ''
        for item in self.raw_data:
            new_line = ','.join(
                (
                item['name'],
                item['surname'],
                item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'w', encoding='UTF8') as f:
            f.write(data)



if __name__=='__main__':
    formatter = FormatData(data)
    formatter_data = formatter.prepare()
    file_wr = FileWriter('fileout.csv')
    file_wr.write(formatter_data)
    print("Смотри выходной файл fileout.csv")