from pathlib import Path

import pyam
from nomenclature import DataStructureDefinition, process

here = Path(__file__).absolute().parent


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Run the validation
    definition = DataStructureDefinition(here / "definitions")
    return process(df, definition)
