"""
Sentinel Data
---------------
Serviço responsável pelo registro
de eventos de auditoria.
"""

from datetime import datetime
from datetime import timezone

from app.audit.models import AuditEvent


def create_audit_event(
    actor_id: str,
    action: str,
    resource_type: str,
    resource_id: str,
    result: str,
    ip_address: str,
    request_id: str,
) -> AuditEvent:
    """
    Cria um evento de auditoria.
    """

    return AuditEvent(

        actor_id=actor_id,

        action=action,

        resource_type=resource_type,

        resource_id=resource_id,

        result=result,

        ip_address=ip_address,

        request_id=request_id,

        timestamp=datetime.now(
            timezone.utc
        ),
    )