# -*- coding: utf-8 -*-
from threading import Thread
import json
import time

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        # Flag to run thread as a deamon
        super(MessageReceiver, self).__init__()
        self.daemon = True
        self.cancelled = False

        # TODO: Finish initialization of MessageReceiver
        self.connection = connection
        self.client = client

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            message = self.connection.recv(2048)
            self.client.receive_message(json.loads(message))

    def cancel(self):
        self.cancelled = False
