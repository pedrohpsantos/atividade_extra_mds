import sys
import os
import unittest

# Adiciona o caminho do diretório 'src' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import add  # Agora isso funcionará

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(add.soma(1, 2), 3)
        self.assertEqual(add.soma(-1, 1), 0)
        self.assertEqual(add.soma(0, 0), 0)

    def test_soma_negative(self):
        self.assertEqual(add.soma(-1, -1), -2)
        self.assertEqual(add.soma(-5, -5), -10)

if __name__ == '__main__':
    unittest.main()
