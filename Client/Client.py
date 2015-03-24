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
        
        login()

        messageReceiver = MessageReceiver(self,self.connection)

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
        # TODO: Handle incoming message #error, info, history, message
        sender = message['sender']
        timestamp = message['timestamp']
        response = message['response']
        content = message['content']
        if response == 'message':
            # Print standard message
            print timestamp +"\n" +response +": " +content
        elif response == 'error':
            # Print error message
            print "Error: " +timestamp +"\n" +sender + ": " +content
        elif response == 'history':
            # Content is all messages previously recieved by the server
            for history_message in content:
                print timestamp +"\n"+ history_message['content']
        elif response == 'info':
            # Print info message
            print "Info:"+timestamp+'\n' + content

        
    def send_payload(self, data):
        # TODO: Handle sending of a payload
        #if (loggingIn):
            #print 'Are you retarded? Log in before you can have fun'
        #    return   
        self.connection.send(json.dumps(data))
        


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
