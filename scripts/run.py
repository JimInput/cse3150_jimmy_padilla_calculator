from pathlib import Path

from cse3150_jimmy_padilla_calculator import Calculator
from cse3150_jimmy_padilla_calculator.file_calculator import FileCalculator

print(Calculator().add(1,2))
print(FileCalculator().sum_file(Path("~/nums.csv").expanduser()))


