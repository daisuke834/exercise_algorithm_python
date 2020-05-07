import unittest
import hoge


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(1, hoge.hoge())


if __name__ == '__main__':
    unittest.main()
