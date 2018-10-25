import socket
import sys
from clients import *
import time

#configuration
BACKLOG     = 5 #maximum number of queued connections. Should be at least 1. It is system-dependent
ClientConnection.MAX_CLIENTS = 20 # max number of connected/accepted clients

#global vars

HOST          = "localhost"
PORT          = 1234
server_socket = None
initialized   = False

"""
    support for IPV6 will be added later.
"""
def start_server(host, port):
    global server_socket
    global initialized
    #TODO make a function to verify if host is of valid format
    #TODO confirm that port is integer in the acceptable port range
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host,port))
        server_socket.listen(BACKLOG)
        initialized = True
    except socket.error as sock_error:
        print (sock_error)
        #TODO handle the error more gracefully or log it.
        print ("[ERROR]: The server failed to bind to %s:%d . Exiting" % (host, port))
        sys.exit(1)
    except:
        print (sys.exc_info())
        print ("[ERROR]: The server failed to bind to %s:%d . Exiting" % (host, port))
        sys.exit(1)
        
               

def accept_connections():
    global server_socket
    global initialized
    if not initialized:
        print("[!] The server is not started. exiting")
        #TODO release any resources
        sys.exit(1)
    while initialized:
        client = server_socket.accept()
        ClientConnection(client)
        time.sleep(0.12)
        #maybe do something if MAX_CLIENTS is reached. I will consider it later
        
start_server(HOST, PORT)
accept_connections()
