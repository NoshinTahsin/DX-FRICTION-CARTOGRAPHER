import os
import time
from typing import Any

from openai import APIConnectionError, APIError, OpenAI, RateLimitError


DEFAULT_MODEL = "gpt-5.1"


def create_json_response(
    *,
    user_message: str,
    instructions: str,
    max_output_tokens: int,
    attempts: int = 3,
) -> str:
    """Call OpenAI and return the response text, retrying transient API failures."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL)

    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            response: Any = client.responses.create(
                model=model,
                instructions=instructions,
                input=user_message,
                max_output_tokens=max_output_tokens,
                text={"format": {"type": "json_object"}},
            )
            return response.output_text
        except (APIConnectionError, APIError, RateLimitError) as e:
            last_error = e
            if attempt == attempts - 1:
                break
            time.sleep(2 ** attempt)

    raise RuntimeError(f"OpenAI API request failed after retry: {last_error}")
