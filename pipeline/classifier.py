# Classifier stage for mapping friction signals to DX dimensions
# Uses OpenAI with dynamic prompts built from config/dimensions.py
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import json
import logging
from typing import List
from pipeline.openai_client import create_json_response
from pipeline.prompts import build_classification_prompt
from config.dimensions import DIMENSIONS
from api.models import FrictionPoint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def classify_friction_points(friction_signals: List[str]) -> List[FrictionPoint]:
    """Classify friction signals against DX dimensions."""
    friction_signals_text = "\n".join(f"- {signal}" for signal in friction_signals)
    prompt = build_classification_prompt()
    user_message = f"{prompt}\n\nFRICTION SIGNALS:\n{friction_signals_text}"

    for attempt in range(2):  # Retry once on failure
        try:
            result_text = create_json_response(
                user_message=user_message,
                max_output_tokens=4000,
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
            
            result = json.loads(result_text)["friction_points"]

            # Validate and filter dimensions
            friction_points = []
            for item in result:
                # Filter out invalid dimension keys
                valid_dimensions = [d for d in item["dimensions"] if d in DIMENSIONS]
                item["dimensions"] = valid_dimensions[:3]  # Max 3 dimensions

                friction_points.append(FrictionPoint(**item))

            return friction_points

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Attempt {attempt + 1} failed with error: {e}")
            logger.error(f"Response text was: {result_text if 'result_text' in locals() else 'EMPTY'}")
            if attempt == 1:  # Second attempt failed
                raise ValueError(f"Failed to classify friction points after retry: {e}")
            # Continue to retry

    raise ValueError("Unexpected error in classification")
