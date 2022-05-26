import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start = None
    
    def __enter__(self):
        self.start = time.perf_counter()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: {:.5f}'.format(time.perf_counter() - self.start))

@contextmanager
def cm_timer_2():
    start = time.perf_counter()
    yield
    print('time: {:.5f}'.format(time.perf_counter() - start))


if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)