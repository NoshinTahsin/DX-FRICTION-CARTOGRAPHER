# Pipeline package for DX Friction Cartographer
from typing import List
from pipeline.extractor import extract_tools_and_friction
from pipeline.classifier import classify_friction_points
from pipeline.synthesizer import synthesize_summary
from api.models import AnalysisResult, ToolInventory, FrictionPoint, DevExSummary

def run_pipeline(transcript: str) -> AnalysisResult:
    """Run the complete 3-stage DX analysis pipeline."""
    # Stage 1: Extract tools and raw friction signals
    tools_inventory, friction_signals = extract_tools_and_friction(transcript)

    # Stage 2: Classify friction signals against dimensions
    friction_points = classify_friction_points(friction_signals)

    # Stage 3: Synthesize summary insights
    devex_summary = synthesize_summary(friction_points)

    return AnalysisResult(
        tools_inventory=tools_inventory,
        friction_points=friction_points,
        devex_summary=devex_summary
    )
