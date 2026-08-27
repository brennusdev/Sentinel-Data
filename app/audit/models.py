"""
Sentinel Data
---------------
Modelo conceitual dos eventos de auditoria.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditEvent:
    """
    Representa uma ação que precisa
    ser registrada para auditoria.
    """

    actor_id: str

    action: str

    resource_type: str

    resource_id: str

    result: str

    ip_address: str

    request_id: str

    timestamp: datetime