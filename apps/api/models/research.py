from dataclasses import dataclass
from datetime import date

@dataclass
class ResearchRecord:
    research_id: str
    company_id: str
    research_date: date
    horizon: str
    thesis: str
    confidence: float
    status: str
