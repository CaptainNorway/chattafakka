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
    loggedIn = False

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
        while True:
            if self.loggedIn:
                request = raw_input("Send request: ")
                if request == 'help':
                    self.help()
                elif request == 'names':
                    self.names()
                elif request == 'logout':
                    self.disconnect()
                else:
                    request = request.split(" ", 1)
                    dictonary = {'request':request[0], 'content':request[1]}
                    self.send_payload(dictonary)
            else:
                self.login()

    def login(self):
        username = raw_input("Skriv brukernavn: ")
        dictonary = {'request':'login','content':username}
        self.send_payload(dictonary)
        self.loggedIn = True

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

    def disconnect(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        self.loggedIn = False
        self.messageReceiver.cancel()
        print "Logged out..."

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

    def help(self):
        print "\t logout - log out"
        print "\t msg <message> - send message"
        print "\t names - list users in chat"
        print "\t help - view help text"
        
    def names(self):
        print "chills"


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
