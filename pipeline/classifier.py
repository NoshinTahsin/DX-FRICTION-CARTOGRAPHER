# Classifier stage for mapping friction signals to DX dimensions
# Uses dynamic prompts built from config/dimensions.py
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import os
import json
import logging
from typing import List
from anthropic import Anthropic
from pipeline.prompts import build_classification_prompt
from config.dimensions import DIMENSIONS
from api.models import FrictionPoint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def classify_friction_points(friction_signals: List[str]) -> List[FrictionPoint]:
    """Classify friction signals against DX dimensions."""
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    friction_signals_text = "\n".join(f"- {signal}" for signal in friction_signals)
    prompt = build_classification_prompt()
    user_message = f"{prompt}\n\nFRICTION SIGNALS:\n{friction_signals_text}"

    for attempt in range(2):  # Retry once on failure
        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=4000,
                temperature=0,
                system="You are a developer experience analyst. Return ONLY valid JSON. No markdown. No explanation. No code fences. Just the raw JSON array.",
                messages=[{"role": "user", "content": user_message}]
            )

            result_text = response.content[0].text
            logger.debug(f"Raw Claude response: {result_text}")
            result_text = result_text.strip()
            
            # Try to extract JSON if there's markdown fencing
            if result_text.startswith("```"):
                result_text = result_text.split("```")[1]
                if result_text.startswith("json"):
                    result_text = result_text[4:]
                result_text = result_text.strip()
            
            result = json.loads(result_text)

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
