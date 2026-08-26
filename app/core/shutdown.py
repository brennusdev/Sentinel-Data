"""
Controle de encerramento seguro.
"""

import signal


class ShutdownManager:

    def __init__(self):

        self.shutdown_requested = False

        signal.signal(
            signal.SIGTERM,
            self.request_shutdown,
        )

        signal.signal(
            signal.SIGINT,
            self.request_shutdown,
        )


    def request_shutdown(
        self,
        signum,
        frame,
    ):

        self.shutdown_requested = True