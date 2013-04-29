from __future__ import print_function, unicode_literals

import logging
import socket

from six.moves import socketserver

log = logging.getLogger(__name__)


class CustomFamilyUDPServer(socketserver.UDPServer):
    def __init__(self, server_address, family, handler_class):
        self.address_family = family
        super(CustomFamilyUDPServer, self).__init__(
            server_address, handler_class,
        )


class BasicTransport(object):
    def __init__(self,
                 on_receive,
                 target_address=None,
                 bind_address=("", 0),
                 family=socket.AF_INET):

        self.target_address = target_address
        self.server = CustomFamilyUDPServer(bind_address, family, None)
        self.server.finish_request = self._handle_packet
        self.on_receive = on_receive

    def _handle_packet(self, request, client_address):
        data, _ = request
        if (self.target_address and client_address != self.target_address):
            log.warn(
                "Ignored packet from unknown address: %s",
                client_address,
                extra={
                    "address": client_address,
                    "data": data,
                },
            )
            return

        self.on_receive(data, client_address)

    def send(self, data, target=None):
        target = target or self.target_address
        return self.server.socket.sendto(data, target)
