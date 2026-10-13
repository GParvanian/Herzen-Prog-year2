
import unittest
from lab2 import add

class  AddTest(unittest.TestCase):
    def test_correct_1(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0,1])
    def test_correct_2(self):
        self.assertEqual(add([3,2,4], 6), [1,2])
    def test_correct_3(self):
        self.assertEqual(add([3,3], 6), [0,1])
    def test_empty(self):
        self.assertEqual(add([], 10), "Подходящих пар нет")
    def test_no_pairs(self):
        self.assertEqual(add([-1,0,1],0), [0,2])
    def test_no_pairs_2(self):
        self.assertEqual(add([0], 1), "Подходящих пар нет")

if __name__ == '__main__':
    unittest.main()

#ДЛЯ ЗАПУСКА ТЕСТОВ
#Из папки lab2 в консоли: python -m test_lab2 -v
