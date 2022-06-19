import os

from dotenv import load_dotenv

load_dotenv()

INITIALISE_WITH_MOCK_DATA = bool(os.getenv("INITIALISE_WITH_MOCK_DATA", False))
