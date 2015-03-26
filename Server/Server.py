# -*- coding: utf-8 -*-
import SocketServer
import Handler
import time
import json
import re

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    loggedIn = False

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        print "Client connected.."

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            received_json = json.loads(received_string)
            request = received_json["request"]
            content = received_json["content"]
            if (content == None):
                print "New request: " + request
            else:
                print "New request: " + request + " " + content
            # TODO: Add handling of received payload from client

            if request == 'login':
                self.username = content
                pattern = re.compile("^[a-zA-Z0-9]*$")
                if self.loggedIn == True:
                    Handler.send_login_error(self, "Already logged in.")
                elif pattern.match(self.username):
                    Handler.login(self,content)
                    self.loggedIn = True
                else:
                    Handler.send_login_error(self, "Invalid username. Letters and numbers only.")
            elif request == 'help':
                Handler.send_help(self)
            elif self.loggedIn == False:
                Handler.send_login_error(self, "You must log in before you can do anything else.")
            elif request == 'logout':
                self.loggedIn = False
                Handler.logout(self)
            elif request == 'msg':
                Handler.recieve_message(content, self.username)
            elif request == 'names':
                Handler.list_users(self)
            elif request == 'history':
                Handler.send_history(self)
            else:
                Handler.send_error(self, request)



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    
    print 'Server running...'
    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
    