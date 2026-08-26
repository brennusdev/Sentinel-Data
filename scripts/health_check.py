"""
Health check utilizado pelo container.
"""

import sys

import urllib.request


URL = (
    "http://localhost:8000/health/live"
)


try:

    response = urllib.request.urlopen(
        URL,
        timeout=3,
    )

    if response.status == 200:

        sys.exit(0)

except Exception:

    pass


sys.exit(1)