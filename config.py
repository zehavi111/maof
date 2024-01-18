from enum import Enum

class ReportEnum(Enum):
    dargot: str = "dargot"
    salaries: str = "highest_salary"
    dargot_salaries: str = "dargot_salaries"

class PopulationEnum(Enum):
    all: str = "all"
    hova: str = "hova"
    keva: str = "keva"