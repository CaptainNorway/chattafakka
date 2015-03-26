import Server
import json
import datetime

client_usernames = []

message_history = []


# Login
def login(client,content):
	username = content
	client_usernames.append((client,username))
	send_history(client)

def logout(client):
	username = None
	for client_user in client_usernames:
		if client_user[0] == client:
			username = client_user[1]
	client_usernames.remove((client,username))

# New message
def recieve_message(message, sender):
	# check if client if logged in first
	data = JSON_ify(message, sender, "message")
	message_history.append(data)
	for client_username in client_usernames:
		client_username[0].connection.send(json.dumps(data))

def list_users(client):
	users = '\t'
	for username in client_usernames:
		users += username[1] + "\n\t"
	data = JSON_ify(users,'server','info')
	client.connection.send(json.dumps(data))

def send_help(client):
	help_message = "\t logout - log out \n\t msg <message> - send message \n\t names - list users in chat \n\t help - view help text"
	data = JSON_ify(help_message,'server','info')
	client.connection.send(json.dumps(data))

def send_error(client, request):
	error_message = request + ' is not a valid request.'
	data = JSON_ify(error_message,'server','error')
	client.connection.send(json.dumps(data))

def send_login_error(client, error_message):
	data = JSON_ify(error_message,'server','error')
	client.connection.send(json.dumps(data))

def send_history(client):
	data = JSON_ify(message_history,'server','history')
	client.connection.send(json.dumps(data))

def JSON_ify(content, sender, response):
	data = {
		'timestamp': str(datetime.datetime.now().strftime('%H.%M.%S')),
		'sender': sender,
		'response': response,
		'content': content
		}
	return data
	