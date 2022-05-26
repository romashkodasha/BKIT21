import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_path("Длинные","Яркие", "С дизайном"),"C:/Users/ASUS/PycharmProjects/Lab5/000")  # add assertion here
    def test_2(self):
        self.assertEqual(find_path("Короткие", "Нюдовые", "С дизайном"), "C:/Users/ASUS/PycharmProjects/Lab5/110")

if __name__ == '__main__':
    unittest.main()
