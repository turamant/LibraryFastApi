class People:
    tool = None

    def __init__(self, name):
        self.name = name

    def setTool(self, tool):
        self.tool = tool

    def write(self, text):
        self.tool.write(self.name, text)


class ToolBase:
    """
    Семейство алгоритмов `Инструмент написания`
    """

    def write(self, name, text):
        raise NotImplementedError()


class PenTool(ToolBase):
    """Ручка"""

    def write(self, name, text):
        print(f'{name} (ручкой) {text}')


class BrushTool(ToolBase):
    """Кисть"""

    def write(self, name, text):
        print(f'{name} (кистью) {text}')


class Student(People):
    """Студент"""
    tool = PenTool()


class Painter(People):
    """Художник"""
    tool = BrushTool()


maxim = Student('Максим')
maxim.write('Пишу лекцию о паттерне Стратегия')
# Максим (ручкой) Пишу лекцию о паттерне Стратегия

sasha = Painter('Саша')
sasha.write('Рисую иллюстрацию к паттерну Стратегия')
# Саша (кистью) Рисую иллюстрацию к паттерну Стратегия

# Саша решил стать студентом
sasha.setTool(PenTool())
sasha.write('Нет, уж лучше я напишу конспект')
# Саша (ручкой) Нет, уж лучше я напишу конспект