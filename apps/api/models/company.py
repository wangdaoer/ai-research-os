from dataclasses import dataclass
from typing import List

@dataclass
class Company:
    company_id: str
    ticker: str
    name: str
    sector: str
    tags: List[str]
