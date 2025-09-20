"""
Created Date: 2025-09-19
Qn: A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a
    given number of rows. Each cell in the spreadsheet can hold an integer
    value between 0 and 105.

    Implement the Spreadsheet class:

    - Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled
      'A' to 'Z') and the specified number of rows. All cells are initially set
      to 0.
    - void setCell(String cell, int value) Sets the value of the specified
      cell. The cell reference is provided in the format "AX" (e.g., "A1",
      "B10"), where the letter represents the column (from 'A' to 'Z') and the
      number represents a 1-indexed row.
    - void resetCell(String cell) Resets the specified cell to 0.
    - int getValue(String formula) Evaluates a formula of the form "=X+Y",
      where X and Y are either cell references or non-negative integers, and
      returns the computed sum.

    Note: If getValue references a cell that has not been explicitly set using
    setCell, its value is considered 0.
Link: https://leetcode.com/problems/design-spreadsheet/
Notes:
"""

import unittest


class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = [[0] * 26 for _ in range(rows)]
        self.ord_a = ord('A')

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.getColRow(cell)
        self.cells[col][row] = value

    def getCell(self, cell: str) -> int:
        col, row = self.getColRow(cell)
        return self.cells[col][row]

    def getColRow(self, cell: str) -> tuple[int, int]:
        return self.ord_a - ord(cell[0]), int(cell[1:])

    def resetCell(self, cell: str) -> None:
        col, row = self.getColRow(cell)
        self.cells[col][row] = 0

    def getValue(self, formula: str) -> int:
        c1, c2 = formula[1:].split('+')
        if c1[0].isalpha():
            c1 = self.getCell(c1)
        else:
            c1 = int(c1)
        if c2[0].isalpha():
            c2 = self.getCell(c2)
        else:
            c2 = int(c2)
        return c1 + c2


class TestSpreadsheet(unittest.TestCase):
    def test2(self):
        s = Spreadsheet(458)
        self.assertEqual(10398, s.getValue('=0126+10272'))

    def test1(self):
        s = Spreadsheet(3)
        self.assertEqual(12, s.getValue('=5+7'))
        s.setCell('A1', 10)
        self.assertEqual(16, s.getValue('=A1+6'))
        s.setCell('B2', 15)
        self.assertEqual(25, s.getValue('=A1+B2'))
        s.resetCell('A1')
        self.assertEqual(15, s.getValue('=A1+B2'))


if __name__ == '__main__':
    unittest.main()
