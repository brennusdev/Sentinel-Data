"""
Cenários oficiais de benchmark.
"""


LOAD_SCENARIOS = {

    "smoke": {

        "events": 1_000,

        "description": (
            "Teste básico de funcionamento."
        ),
    },

    "normal": {

        "events": 100_000,

        "description": (
            "Carga normal."
        ),
    },

    "stress": {

        "events": 1_000_000,

        "description": (
            "Teste de estresse."
        ),
    },
}