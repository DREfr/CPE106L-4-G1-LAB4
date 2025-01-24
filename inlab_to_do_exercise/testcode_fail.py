import code
import unittest

class TestCode(unittest.TestCase):
    def testsimple(self):
        self.assertEqual(code.return_zero(), 0)

    def testdouble(self):
        self.assertEqual(code.double_number(2), 4)
        self.assertEqual(code.double_number(4), 8)
        self.assertEqual(code.double_number(0), 0)
        self.assertEqual(code.double_number(-2), 4)  # Intentional error

if __name__ == '__main__':
    unittest.main()
