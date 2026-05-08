# Synthesizer stage for summary generation from classified friction points
# Uses OpenAI API to create insights and output formats
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import json
import logging
from typing import List
from pipeline.openai_client import create_json_response
from pipeline.prompts import build_synthesis_prompt
from api.models import DevExSummary, FrictionPoint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def synthesize_summary(friction_points: List[FrictionPoint]) -> DevExSummary:
    """Generate DevEx summary from classified friction points."""
    # Convert friction points to JSON for prompt
    friction_points_data = [fp.dict() for fp in friction_points]
    friction_points_text = json.dumps(friction_points_data, indent=2)

    prompt = build_synthesis_prompt()
    user_message = f"{prompt}\n\nFRICTION POINTS:\n{friction_points_text}"

    for attempt in range(2):  # Retry once on failure
        try:
            result_text = create_json_response(
                user_message=user_message,
                max_output_tokens=2000,
                instructions="You are a developer experience analyst. Return only valid JSON matching the requested object shape.",
            )

            logger.debug(f"Raw OpenAI response: {result_text}")
            result_text = result_text.strip()
            
            # Try to extract JSON if there's markdown fencing
            if result_text.startswith("```"):
                result_text = result_text.split("```")[1]
                if result_text.startswith("json"):
                    result_text = result_text[4:]
                result_text = result_text.strip()
            
            result = json.loads(result_text)

            return DevExSummary(**result)

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Attempt {attempt + 1} failed with error: {e}")
            logger.error(f"Response text was: {result_text if 'result_text' in locals() else 'EMPTY'}")
            if attempt == 1:  # Second attempt failed
                raise ValueError(f"Failed to synthesize summary after retry: {e}")
            # Continue to retry

    raise ValueError("Unexpected error in synthesis")
