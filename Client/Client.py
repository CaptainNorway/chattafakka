# -*- coding: utf-8 -*-
import socket
import MessageReceiver
import json
import os
import platform

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.server_port = server_port
        self.run()
        self.messageReceiver = MessageReceiver.MessageReceiver(self,self.connection)
        self.messageReceiver.start()
        print "login <username> - log in with username"
        print "logout - log out"
        print "msg <message> - send message"
        print "names - list users in chat"
        print "help - view help text"
        print "history - view log of all sent messages"
        while True:
            request = raw_input('')
            if request == 'logout':
               self.disconnect()
            else:
                if ' ' in request:
                    request = request.split(' ', 1)
                    dictonary = {'request':request[0], 'content':request[1]}
                else:
                   dictonary = {'request':request, 'content':None}
                self.send_payload(dictonary)

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

    def disconnect(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        self.loggedIn = False
        dictonary = {'request':'logout','content':None}
        self.send_payload(dictonary)
        self.messageReceiver.cancel()
        print "Logged out..."

    def receive_message(self, message):
        # TODO: Handle incoming message #error, info, history, message
        sender = message["sender"]
        timestamp = message["timestamp"]
        response = message["response"]
        content = message["content"]
        if response == 'message':
            # Print standard message
            print timestamp + " " + sender +": " +content
        elif response == 'error':
            # Print error message
            print timestamp + " ERROR - " +content
        elif response == 'history':
            # Content is all messages previously recieved by the server
            for history_message in content:
                print "\t" + history_message['timestamp'] + " " + history_message['sender'] +": " + history_message['content']
        elif response == 'info':
            # Print info message
            print content
        else:
            print "Repsonse not recognized."

        
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
