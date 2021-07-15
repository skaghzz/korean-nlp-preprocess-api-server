from unittest import TestCase
from app.modules.preprocess.clean_text import clean_text


class Test(TestCase):
    def test_clean_text(self):
        text = ["어우지금##입12321니다. 아니22요. 강하다.", "댈저해두제더"]
        result = clean_text(text)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) == 2)
