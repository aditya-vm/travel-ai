from pydantic import BaseModel
from typing import List


class OptimizationResult(BaseModel):
    warnings: List[str]
    tips: List[str]
    layover_analysis: List[str]
    travel_stress_score: int
    fatigue_level: str