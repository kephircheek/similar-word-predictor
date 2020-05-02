from simsyn import Synonymizer

import unittest

class Core(unittest.TestCase):


    def test_predict(self):
        self.assertIsInstance(
            Synonymizer().predict('word'),
            list
        )
