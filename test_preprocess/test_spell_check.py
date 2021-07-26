import unittest
from preprocess.spell_check import spell_check


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = ["어우지금##입12321니다. 아니22요. 강하다.", "댈저해두제더"]
        result = spell_check(text)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) == 2)


if __name__ == '__main__':
    unittest.main()
