# built in
from pathlib import Path

#pip installed

#our package
# from ..calculator import Calculator
from cse3150_jimmy_padilla_calculator.calculator import Calculator

class FileCalculator(Calculator):
    def sum_file(self, path=None) -> int:
        if path is None:
            path = Path(__file__).parent / "nums.csv"
        total = 0
        with path.open() as f:
            for line in f:
                total += int(line)
        return total

