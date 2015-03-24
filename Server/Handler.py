import Server
import json
import datetime

client_usernames = []

message_history = []


# Login
def login(client,content):
	username = content
	client_usernames.append((client,username))

def logout(client):
	client_usernames.remove(client)

# New message
def recieve_message(message, sender):
	# check if client if logged in first
	message_history.append(message)
	data = JSON_ify(message)
	for client_username in client_usernames:
		client_username[0].connection.send(JSON.dumps(data))

def list_users(client):
	users = ''
	for username in client_usernames:
		users += username[1] + ","
	data = JSON_ify(users,'server','info')
	client.connection.send(data)

def send_help(client):
	help_message = "Ikkje ver retard"
	data = JSON_ify(help_message,'server','info')
	client.connection.send(data)

def send_error(client):
	error_message = 'Syntax error in command'
	data = JSON_ify(error_message,'server','info')
	client.connection.send(data)

def  JSON_ify(content, sender, response):
	data = {
		'timestamp': datetime.now,
		'sender': sender,
		'response': response,
		'content': content
		}
	return data
	