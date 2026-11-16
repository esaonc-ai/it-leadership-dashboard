"""Regression checks for the weekly workbook's exact-text RAG rules."""
import unittest

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import PatternFill

from refresh_dashboard import evaluate_expression, source_style


class RagExpressionTests(unittest.TestCase):
    def setUp(self):
        self.sheet = Workbook().active
        self.sheet['D4'] = 'Amber'
        self.sheet['D5'] = 'Green'

    def test_equality_is_case_insensitive_and_exact(self):
        self.assertTrue(evaluate_expression('$D4="aMbEr"', self.sheet))
        self.assertFalse(evaluate_expression('$D4="Red"', self.sheet))
        self.assertFalse(evaluate_expression('$D4="Amb"', self.sheet))

    def test_priority_translation_and_stop_if_true(self):
        for word, fill in [('Amber', 'FFF2CC'), ('Green', 'C6E0B4')]:
            self.sheet.conditional_formatting.add('D4:D5', FormulaRule(
                formula=[f'$D4="{word}"'], stopIfTrue=True,
                fill=PatternFill('solid', fgColor=fill)))
        self.assertEqual(source_style(self.sheet['D4'])[0], '#FFF2CC')
        self.assertEqual(source_style(self.sheet['D5'])[0], '#C6E0B4')

    def test_existing_search_expression(self):
        self.assertTrue(evaluate_expression(
            'AND(ISNUMBER(SEARCH("amber",D4)),D4<>"")', self.sheet))

    def test_unsupported_expression_still_blocks(self):
        with self.assertRaises(ValueError):
            evaluate_expression('SUM(D4:D5)>0', self.sheet)


if __name__ == '__main__':
    unittest.main()
