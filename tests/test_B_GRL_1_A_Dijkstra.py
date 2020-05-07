import unittest
import B_GRL_1_A_Dijkstra
import sys
import io
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.org_stdout, sys.stdout = sys.stdout, io.StringIO()

    def tearDown(self):
        sys.stdout = self.org_stdout

    def test_call_dijkstra_algorithm_1(self):
        inputs = ['4 5 0',
                  '0 1 1',
                  '0 2 4',
                  '1 2 2',
                  '2 3 1',
                  '1 3 5']
        answer = '0\n' \
                 '1\n' \
                 '3\n' \
                 '4\n'

        with patch('builtins.input', side_effect=inputs):
            B_GRL_1_A_Dijkstra.call_dijkstra_algorithm()
        self.assertEqual(answer, sys.stdout.getvalue())

    def test_call_dijkstra_algorithm_2(self):
        inputs = ['4 6 1',
                  '0 1 1',
                  '0 2 4',
                  '2 0 1',
                  '1 2 2',
                  '3 1 1',
                  '3 2 5']

        answer = '3\n' \
                 '0\n' \
                 '2\n' \
                 'INF\n'
        with patch('builtins.input', side_effect=inputs):
            B_GRL_1_A_Dijkstra.call_dijkstra_algorithm()
        self.assertEqual(answer, sys.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
