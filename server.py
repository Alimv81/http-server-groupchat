import os
import json
import time
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

# Dictionary to store chat messages
chat_messages = []

# Define the request handler
class ChatHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get_messages':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Send the chat messages as JSON
            self.wfile.write(json.dumps(chat_messages).encode())
        else:
            # Serve static files
            super().do_GET()

    def do_POST(self):
        if self.path == '/send_message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            message_data = parse_qs(post_data)
            message = message_data['message'][0]
            chat_messages.append(message)
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Message sent successfully'.encode())

    def do_DELETE(self):
        if self.path == '/delete_messages':
            # Handle the request to delete chat messages
            chat_messages.clear()
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Chat messages deleted successfully'.encode())

# Create the server
with socketserver.TCPServer(('localhost', 8080), ChatHandler) as httpd:
    print('Chat server is running at http://localhost:8080')
    print('you can open multiply instances of the chat clients in your browser and use them to send messages')
    n = int(input('enter the number of instances you want to open in the browser:'))
    time.sleep(3)
    for _ in range(n):
        os.system('cmd /c start chrome "http://localhost:8080/group_chat.html"')
    httpd.serve_forever()
