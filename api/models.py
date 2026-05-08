# Pydantic models for API request and response payloads
from pydantic import BaseModel
from typing import List

class ToolInventory(BaseModel):
    stage: str
    tools: List[str]
    notes: str

class FrictionPoint(BaseModel):
    stage: str
    friction_label: str
    example: str
    how_often: str  # Daily|Weekly|Occasionally|Rarely
    pain_level: int  # 1-5
    who_affects: str
    justification: str
    dimensions: List[str]  # dimension keys from dimensions.py

class DevExSummary(BaseModel):
    most_affected_dimensions: List[str]
    highest_pain_stage: str
    total_friction_points: int

class AnalysisResult(BaseModel):
    tools_inventory: List[ToolInventory]
    friction_points: List[FrictionPoint]
    devex_summary: DevExSummary

class AnalyzeRequest(BaseModel):
    transcript: str
