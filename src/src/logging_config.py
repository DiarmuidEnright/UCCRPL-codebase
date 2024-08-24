import logging
from typing import Any

def setup_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("rocket_system.log"),
            logging.StreamHandler()
        ]
    )
    logger: logging.Logger = logging.getLogger(__name__)
    return logger

logger: logging.Logger = setup_logging()
