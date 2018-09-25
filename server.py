import socket
import sys

#configuration
BACKLOG     = 5 #maximum number of queued connections. Should be at least 1. It is system-dependent
MAX_CLIENTS = 20 # max number of connected/accepted clients

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
        pass
    except:
        pass

def accept_connections():
    global server_socket
    if not initialized:
        print("[!] The server is not started. exiting")
        #TODO release any resources
        sys.exit(1)
    while initialized:
        client = server_socket.accept()
        #to be continued
        
start_server(HOST, PORT)
accept_connections()
