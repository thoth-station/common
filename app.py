import logging
from thoth.common import init_logging

init_logging()
_LOGGER = logging.getLogger("test")

try:
   raise ValueError("My really dope error")
except ValueError:
    _LOGGER.exception("exception raised")