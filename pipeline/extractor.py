# Extractor stage for raw transcript processing
# Uses OpenAI API to extract tools and friction signals from transcripts
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import json
import logging
from typing import List
from pipeline.openai_client import create_json_response
from pipeline.prompts import build_extraction_prompt
from api.models import ToolInventory

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_tools_and_friction(transcript: str) -> tuple[List[ToolInventory], List[str]]:
    """Extract tools inventory and raw friction signals from transcript."""
    prompt = build_extraction_prompt()
    user_message = f"{prompt}\n\nTRANSCRIPT:\n{transcript}"

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
            
            result = json.loads(result_text)

            # Validate structure
            tools_inventory = [ToolInventory(**item) for item in result["tools_inventory"]]
            friction_signals = result["friction_signals"]

            return tools_inventory, friction_signals

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Attempt {attempt + 1} failed with error: {e}")
            logger.error(f"Response text was: {result_text if 'result_text' in locals() else 'EMPTY'}")
            if attempt == 1:  # Second attempt failed
                raise ValueError(f"Failed to extract tools and friction after retry: {e}")
            # Continue to retry

    raise ValueError("Unexpected error in extraction")
