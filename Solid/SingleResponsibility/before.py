preambula = '''
            Один класс выполняет два метода(ответственности)Б
            требуется разделить ответстевноость .
            Разделим класс на два:
            - один подготтавливает данные,
            - другой выводит в файл
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

class ExportCsv:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result

    def write_file(self, filename):
        with open(filename, 'w', encoding='UTF8') as f:
            f.write(self.data)


if __name__=='__main__':
    print(preambula)
    exporter = ExportCsv(data)
    exporter.write_file('out.csv')
    print("Смотри выходной файл out.csv")