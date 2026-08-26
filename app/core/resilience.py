"""
Mecanismos de resiliência da aplicação.
"""

import time


class CircuitBreaker:
    """
    Implementação simples de Circuit Breaker.
    """

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 30,
    ):

        self.failure_threshold = (
            failure_threshold
        )

        self.recovery_timeout = (
            recovery_timeout
        )

        self.failure_count = 0

        self.state = "CLOSED"

        self.opened_at = None


    def record_success(self):
        """
        Registra uma operação bem-sucedida.
        """

        self.failure_count = 0

        self.state = "CLOSED"

        self.opened_at = None


    def record_failure(self):
        """
        Registra uma falha.
        """

        self.failure_count += 1

        if (
            self.failure_count
            >= self.failure_threshold
        ):

            self.state = "OPEN"

            self.opened_at = time.monotonic()


    def allow_request(self) -> bool:
        """
        Determina se uma operação pode acontecer.
        """

        if self.state == "CLOSED":

            return True


        if self.state == "OPEN":

            elapsed = (
                time.monotonic()
                - self.opened_at
            )

            if (
                elapsed
                >= self.recovery_timeout
            ):

                self.state = "HALF_OPEN"

                return True

            return False


        return True