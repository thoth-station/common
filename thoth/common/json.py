import json
import datetime


class SafeJSONEncoder(json.JSONEncoder):
    """Convert objects to JSON, safely."""

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return repr(o)
