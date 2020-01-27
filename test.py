import sys
import logging
import inspect
# from thoth.common import init_logging

# init_logging()
# _LOGGER = logging.getLogger("test")

from lib1 import Test as Test1
from lib2 import Test as Test2

try:
    raise Test2
except Exception:
    #_LOGGER.exception("exception ignored 1")
    exc_type, exc_val, tb = sys.exc_info()
    print(sys.exc_info())
    exc_t = exc_type.__dict__
    print(vars(exc_type))
    print(inspect.getmodule(exc_type))
    print(getattr(exc_type, "__module__")+'.'+exc_type.__name__)
    print(str(sys.exc_info()[0]))
    print(sys.exc_info()[0].__name__)
    print(sys.exc_info()[0].__qualname__)