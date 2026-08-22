# commit_log_agent/fallback.py

import logging
import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError
from typing import Optional


# Create a logger for this module.
# It lets us record when the fallback model is used.
logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# MODEL TIERS
# ---------------------------------------------------------

# The model we normally want to use.
PRIMARY_MODEL = "gpt-4o"
# The cheaper backup model.
FALLBACK_MODEL = "gpt-4o-mini"


# ---------------------------------------------------------
# FALLBACK FUNCTION
# ---------------------------------------------------------

def call_with_fallback(
    client: OpenAI,
    messages: list,
    tools: Optional[list] = None
) -> tuple:

    """
    Try the primary model first.

    If it fails because of a rate limit or connection problem,
    try the fallback model.

    Returns:
        response, model_used
    """

    # Try the models in this order:
    # 1. Primary model
    # 2. Fallback model
    for model in (PRIMARY_MODEL, FALLBACK_MODEL):

        try:

            # Make the API call using the current model.
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools or [],
            )

            # If we reached the fallback model,
            # tell us that degradation happened.
            if model != PRIMARY_MODEL:

                logger.warning(
                    f"Primary model unavailable. "
                    f"Responded using fallback: {model}"
                )

            # Return BOTH:
            # - the response
            # - the model that actually produced it
            return response, model


        # Only these errors trigger fallback.
        except (RateLimitError, APIConnectionError) as exc:

            # If the fallback model also failed,
            # there is nothing else to try.
            if model == FALLBACK_MODEL:

                logger.error(
                    f"Both primary and fallback models failed. "
                    f"Last error: {exc}"
                )

                raise

            # The primary model failed,
            # so try the fallback model.
            logger.warning(
                f"Primary model {model} failed ({exc}). "
                f"Trying fallback."
            )


    # This should never be reached.
    raise RuntimeError(
        "Fallback logic exhausted without returning or raising."
    )



# ---------------------------------------------------------
# TEMPORARY TEST — Fallback behaviour
# ---------------------------------------------------------

if __name__ == "__main__":

    # Create the OpenAI client
# Load the API key from the .env file
    load_dotenv()

    # Create the OpenAI client using the API key
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
    # Simple test message
    messages = [
        {
            "role": "user",
            "content": "Say hello in one word."
        }
    ]

    try:

        # Try the primary model.
        # Because we deliberately gave it an invalid name,
        # the fallback should be triggered.
        response, model_used = call_with_fallback(
            client,
            messages
        )

        # Show which model actually answered
        print(f"Model used: {model_used}")

        # Show the response
        print(response.choices[0].message.content)

    except Exception as e:

        # Show the error if both models fail
        print(f"Fallback test failed: {e}")