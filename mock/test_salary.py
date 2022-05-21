import unittest
from unittest import mock
from unittest.mock import MagicMock
import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2022)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)

        # 本当に呼ばれたかコールされているかを確認する
        s.bonus_api.bonus_price.assert_called()

        # 一度だけコールされているかを確認する
        s.bonus_api.bonus_price.assert_called_once()

        # 引数を正しく渡せているかを確認する
        s.bonus_api.bonus_price.assert_called_with(year=2022)

        # 引数を正しく渡せているかを確認する
        s.bonus_api.bonus_price.assert_called_once_with(year=2022)

        # 何回呼ばれているか
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

        # 呼ばれていないかを確認するとき
        # s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('salary.ThirdPartyBonusApi.bonus_price',
                return_value=1)
    def test_calculation_salary_patch(self, mock_bouns):
        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(), 101)
        mock_bouns.assert_called()
        mock_bouns.assert_called_once()
        mock_bouns.assert_called_with(year=2022)
        self.assertEqual(mock_bouns.call_count, 1)

    @mock.patch('salary.ThirdPartyBonusApi.bonus_price')
    def test_calculation_salary_patch2(self, mock_bouns):
        # mockの返却値
        mock_bouns.return_value = 1
        # 関数呼び出し
        s = salary.Salary(year=2022)
        salary_price = s.calculation_salary()
        # テスト
        self.assertEqual(salary_price, 101)
        mock_bouns.assert_called()
