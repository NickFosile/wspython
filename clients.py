import socket
import sys
from threading import Thread

class Protocol():

    packet_start = b"<begin>"
    packet_end   = b"<end>"
    #the idea here is to implement the websocket protocol, including the websocket client/server hello etc
    #this is for testing purposes, I will implement the protocol later.

    @staticmethod
    def closing_msg():
        return Protocol.packet_start + b"closing connection" + Protocol.packet_end

class ClientConnection(Thread):

    clientPool = []
    MAX_CLIENTS = 20
    

    def __init__(self, accepted_client):
        Thread.__init__(self)
        self.connection = accepted_client[0]
        self.ip = accepted_client[1][0]
        self.port = accepted_client[1][1]
        self.alive = False
        
        if len(ClientConnection.clientPool) >= ClientConnection.MAX_CLIENTS:
            try:
                #the Protocol object is a class that will implement the ws protocol. I will fix it after I am done with sockets.
                self.connection.send(Protocol.closing_msg())
                self.connection.shutdown(socket.SHUT_RDWR)
                self.connection.close()
                print ("[!] Client from %s:%d was refused due to full client pool" % (self.ip, self.port))
                del self.connection
                del ip
                return
            except:
                print ("[ERROR] on closing client " + sys.exc_info())
                self.connection.close()
                del self.connection
                return
        self.start()


    def run(self):
        temp_counter = 0
        if self.alive == False:
            #do any client validation you want here, and set alive to True afterwards
            ClientConnection.clientPool.append(self)
            self.alive = True
            print ("[*] Client from %s:%d was accepted" % (self.ip, self.port))

        while self.alive and temp_counter < 5:
            #for now i will only print on screen what the client sends. later i will implement a protocol
            response = self.connection.recv(4096)
            if response == b"" or response == None:
                self.dispose()
                print ("[*] Client %s:%d DISCONNECTED. " % (self.ip, self.port))
                break
            print ("[CLIENT MSG]:FROM %s:%d %s " % (self.ip, self.port, response))
            temp_counter += 1

    def dispose(self):
        self.connection.shutdown(socket.SHUT_RDWR)
        self.connection.close()
        self.alive = False # terminate thread
        del self.connection
                   
        
            
            
        
