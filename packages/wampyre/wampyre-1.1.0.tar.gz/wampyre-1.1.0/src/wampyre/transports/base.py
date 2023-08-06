from abc import ABC, abstractmethod

from ..session import Session


class TransportBase(ABC):
    def __init__(self):
        self.session = Session(self)

    @abstractmethod
    def send(self, opcode, *args):
        """Send a command to a client"""

    @abstractmethod
    def realm_allowed(self, realm):
        """Check if a transport can access a realm"""

    @abstractmethod
    def close_session(self):
        """Close a session"""

    def receive(self, *args):
        self.session.handle_command(*args)

    def session_lost(self):
        self.session.close_session()

    @abstractmethod
    def method_uri_allowed(self, method, uri):
        """Check if method and uri call is allowed by this transport"""
