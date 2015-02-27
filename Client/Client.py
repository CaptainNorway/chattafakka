# -*- coding: utf-8 -*-
import socket
import MessageReceiver

class Client:
    """
    This is the chat client class
    """
    loggedIn = 0

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.run()
        
        messageReceiver = MessageReceiver(self,self.connection)

        login()


    def login():
        username = raw_input("Skriv brukernavn: ")
        dictonary = {'request':'login','content':username}
        send_payload(dictonary)

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

    def disconnect(self):
        # TODO: Handle disconnection
        pass

    def receive_message(self, message):
        # TODO: Handle incoming message
        sender = message['sender']
        timestamp = message['timestamp']
        response = message['response']
        content = message['content']
        if(response != 'message'):
            print timestamp +"\n" +response +": " +content
        else:
            print timestamp +"\n" +sender + ": " +content
            
        
    def send_payload(self, data):
        # TODO: Handle sending of a payload
        if (! loggedIn and ! data['request']= 'login'):
            print 'Are you retarded? Log in before you can have fun'
            return   
        self.connection.send(json.dumps(data))
        pass


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
