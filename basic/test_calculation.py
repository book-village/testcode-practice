import unittest

from pip import main
import calculation


class CalTest(unittest.TestCase):
    def test_add_num_and_double関数の動作確認(self):
        cal = calculation.Cal()
        # 正しく計算されていることを確認
        self.assertEqual(cal.add_num_and_double(1, 1), 4)
        self.assertNotEqual(cal.add_num_and_double(1, 1), 5)

    def test_add_num_and_double関数の例外処理を確認(self):
        # str型の引数を与えて、ValueErrorが発生することを確認する
        cal = calculation.Cal()
        with self.assertRaises(ValueError) as ex:
            cal.add_num_and_double("1", "1")
        self.assertEqual(ex.exception.args[0], '引数が異常です。')