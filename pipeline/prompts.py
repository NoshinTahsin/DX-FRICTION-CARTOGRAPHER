# Dynamic prompt builder for AI API calls
# All prompt content must be derived from config/dimensions.py
from config.dimensions import DIMENSIONS

def build_extraction_prompt() -> str:
    stages = ["Planning", "Coding", "Reviewing", "Testing", "Deployment", "Observability"]
    stages_text = ", ".join(stages)

    prompt = f"""Extract tools and friction signals from the transcript.

STAGES: {stages_text}

For each stage mentioned in the transcript, list all tools and technologies used.
Also extract all friction signals (problems, frustrations, inefficiencies).
If the transcript does not mention any tools, return an empty tools_inventory array.
If the transcript does not mention any problems, frustrations, or inefficiencies, return an empty friction_signals array.

Return ONLY valid JSON like this:
{{"tools_inventory": [{{"stage": "Planning", "tools": ["Jira"], "notes": "vague"}}, {{"stage": "Coding", "tools": ["VS Code"], "notes": "slow"}}], "friction_signals": ["Requirements change constantly", "Reviews are slow"]}}

Extract from the transcript and return only JSON, no other text."""

    return prompt

def build_classification_prompt() -> str:
    # Build flat dimension list dynamically
    dimension_descriptions = []
    for key, dim in DIMENSIONS.items():
        desc = f"- {key}: {dim['prompt_description']}"
        dimension_descriptions.append(desc)

    dimensions_text = "\n".join(dimension_descriptions)

    prompt = f"""Classify each friction signal against DX dimensions.

DX DIMENSIONS:
{dimensions_text}

For each friction signal, assign 1-3 dimensions that are clearly affected.
Infer stage, how_often, pain_level (1-5), and who_affects from context.
Also include a concise justification explaining the transcript evidence behind the frequency, pain level, affected people, and selected dimensions.

Return ONLY valid JSON object like this:
{{"friction_points": [{{"stage": "Planning", "friction_label": "Unclear requirements", "example": "Requirements change mid-sprint", "how_often": "Weekly", "pain_level": 4, "who_affects": "All developers", "justification": "The transcript says requirements change mid-sprint and uses team-wide language, so this affects shared goal clarity and flow.", "dimensions": ["goal_clarity", "flow_state"]}}, {{"stage": "Testing", "friction_label": "Flaky tests", "example": "Tests fail randomly", "how_often": "Daily", "pain_level": 5, "who_affects": "All developers", "justification": "The transcript says tests fail randomly and nobody trusts them, indicating frequent team-wide feedback-loop friction.", "dimensions": ["feedback_loops"]}}]}}

Return only JSON object, no other text."""

    return prompt

def build_synthesis_prompt() -> str:
    prompt = """Analyze friction points and create a DevEx summary.

Count dimensions by frequency. Find stage with highest average pain_level.

Return ONLY valid JSON like this:
{{"most_affected_dimensions": ["feedback_loops", "flow_state", "goal_clarity", "cognitive_load", "frictionless_releases"], "highest_pain_stage": "Testing", "total_friction_points": 10}}

Return only JSON object, no other text."""

    return prompt
