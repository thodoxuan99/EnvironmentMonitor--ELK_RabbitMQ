from sys import version as python_version
from cgi import parse_header, parse_multipart
from http.server import BaseHTTPRequestHandler , HTTPServer
import socketserver
if python_version.startswith('3'):
    from urllib.parse import parse_qs
    from http.server import BaseHTTPRequestHandler
else:
    from urlparse import parse_qs
    from BaseHTTPServer import BaseHTTPRequestHandler
import threading
import json
import time
import paho.mqtt.client as mqtt
client = mqtt.Client()
PORT = 8000
temperature = 0
humidity = 0
light = 0
deviceID=""
ip = ""
TimeStamp=""
RoomName =""

def on_connect(client, userdata, flags, rc):
    print("Connected to the RabbitMQ Broker")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.ar

# The callback for when a PUBLISH message is received from the server.
def on_disconnect(client,userdata,rc):
    client.connect("localhost", 1883, 60)
def setMQTTConnect():
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.username_pw_set("logUser","logPwd")
    client.connect("localhost", 1883, 60)
def keepConnect2Broker():
    client.loop_forever()
    pass
def publish(key , message):
    client.publish(key,message)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if (self.path=='/'):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write('Request OK'.encode())
        elif self.path=='/config':
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write('Request OK'.encode())
            length = int(self.headers['content-length'])
            message = self.rfile.read(length).decode("utf-8")
            print(message)
            publish("environment",message)




    def do_POST(self):
        if (self.path=='/collectData'):
            length = int(self.headers['content-length'])
            message = self.rfile.read(length).decode("utf-8")
            print(message)
            publish("environment",message)
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write('Hello'.encode())

def HTTP_Server():
    server = HTTPServer(('localhost',PORT),Handler)
    server.serve_forever()
    pass

if __name__ == '__main__':
    setMQTTConnect()
    http = threading.Thread(target=HTTP_Server)
    mqtt = threading.Thread(target=keepConnect2Broker)
    http.start()
    mqtt.start()
    http.join()
    mqtt.join()