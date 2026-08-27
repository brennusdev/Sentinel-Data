"""
Sentinel Data
---------------
Define os papéis e permissões
existentes no sistema.
"""

from enum import Enum


class Role(str, Enum):
    """
    Papéis disponíveis no Sentinel.
    """

    ADMIN = "admin"

    PROCESSOR = "processor"

    VIEWER = "viewer"


# Cada papel recebe um conjunto
# específico de permissões.
ROLE_PERMISSIONS = {

    Role.ADMIN: {
        "events:read",
        "events:write",
        "events:delete",
        "audit:read",
        "users:manage",
    },

    Role.PROCESSOR: {
        "events:read",
        "events:write",
    },

    Role.VIEWER: {
        "events:read",
    },
}