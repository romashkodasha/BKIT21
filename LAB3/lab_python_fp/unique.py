# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = set()
        self.iter = iter(items)
        self.ignore_case = kwargs.get('ignore_case', True)
        self.lower_set = set()

    def __next__(self):
        current = None
        while True:
            current = str(next(self.iter))
            if not self.ignore_case and current not in self.data: 
                self.data.add(current)
                return current
            elif self.ignore_case and current.lower() not in self.lower_set: 
                self.data.add(current)
                self.lower_set.add(current.lower())
                return current

    def __iter__(self):
        return self


if __name__ == "__main__":
    b = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    alist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    
    for i in Unique(b): print(i)
    print()
    for i in Unique(b, ignore_case=False): print(i)