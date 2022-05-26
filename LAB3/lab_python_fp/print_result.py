
def print_result(func):
    def wrapper(self=None):
        print(func.__name__)
        if self: self = func(self) 
        else: self = func()
        if isinstance(self,dict):
            for key,val in self.items():
                print(key,"=",val,end='\n')
        elif isinstance(self,list):
            print(*self,sep='\n')
        else:
            print(self)
        return self
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()









