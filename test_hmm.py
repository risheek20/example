from unittest import TestCase
import hmm


class Test(TestCase):
    def test_add(self):
        result=hmm.add(2,3)
        self.assertEqual(result,5)

