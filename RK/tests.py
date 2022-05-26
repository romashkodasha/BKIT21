from data import *
from main import task1, task2, task3
import unittest


class Tests(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1(), [('Assembly', 1949, 'Android Studio')])

    def test_task2(self):
        self.assertEqual(task2(), [('Visual Studio', 1995), ('Visual Studio Code', 1983), ('Android Studio', 1949)])

    def test_task3(self):
        self.assertEqual(task3(), [('Pascal', 'Android Studio'), ('Java', 'Android Studio'), ('Python', 'Visual Studio'), ('C++', 'Visual Studio'), ('Assembly', 'Visual Studio'), ('C++', 'Visual Studio Code')])


if __name__ == '__main__':
    unittest.main()

