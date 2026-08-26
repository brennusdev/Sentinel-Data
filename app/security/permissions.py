"""
Permissões utilizadas pelo Sentinel Data.
"""

from enum import Enum


class Role(str, Enum):

    ADMIN = "admin"

    PROCESSOR = "processor"

    VIEWER = "viewer"


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