"""Simple interface for retrieving the OpenAI API key.

This module exposes `get_api_key()` which reads the required
`OPENAI_API_KEY` environment variable. It raises a `RuntimeError`
or logs a warning if the key is missing.
"""

import os
import logging

logger = logging.getLogger(__name__)


def get_api_key() -> str:
    """Return the OpenAI API key or raise ``RuntimeError`` if not set."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        logger.warning("OPENAI_API_KEY environment variable is not set")
        raise RuntimeError(
            "OPENAI_API_KEY environment variable must be set to authenticate with OpenAI." 
        )
    return key


if __name__ == "__main__":
    # Example usage: just fetch and print the key (if configured).
    print(get_api_key())
