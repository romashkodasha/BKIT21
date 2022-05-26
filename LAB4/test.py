from main import *
import unittest

class TestQr(unittest.TestCase):
    def setUp(self):
        self.get_coef = get_coef
        self.get_roots = get_roots
    def test_roots(self):
        self.assertTrue(len(self.get_roots(0, 0, 0)) > 4)
        self.assertEqual(self.get_roots(1, 1, 1), [])
        self.assertEqual(self.get_roots(-1, -1, -1), [])
        self.assertEqual(self.get_roots(0, 0, 1), [])
        self.assertEqual(self.get_roots(1, 0, 0), [0,])
        self.assertEqual(self.get_roots(0, 1, 0), [0,])
        self.assertEqual(self.get_roots(1, 0, 1), [])
        self.assertEqual(self.get_roots(0, 1, 1), [])
        self.assertEqual(self.get_roots(10, 25, 0), [0,])

        self.assertEqual(set(self.get_roots(0, 1, -16)), {-4, 4})
        self.assertEqual(set(self.get_roots(1, 0, -4)), {-2 ** 0.5, 2 ** 0.5})
        self.assertEqual(set(self.get_roots(1, -5, -36)), {-3, 3})
        self.assertEqual(set(self.get_roots(1, 14, 48)), set([]))
        self.assertEqual(set(self.get_roots(1, 1, -20)), {-2, 2})
        self.assertEqual(set(self.get_roots(1, -5, 4)), {-2, -1, 1, 2})


if __name__ == '__main__':
    unittest.main()
