"""
Health check utilizado pelo container.
"""

import sys
import urllib.request


HEALTH_URL = (
    "http://localhost:8000/health/live"
)


def main() -> None:
    """
    Verifica se a API está respondendo.
    """

    try:

        response = urllib.request.urlopen(
            HEALTH_URL,
            timeout=3,
        )

        if response.status == 200:

            sys.exit(0)

    except Exception:

        pass

    sys.exit(1)


if __name__ == "__main__":

    main()