#!/usr/bin/env python

import socket
import threading
import queue
import sys
import time
import signal
import pickle

'''
The Sqwackchat server class is used to make a multi client server object that
manages the connections of qwackchat clients.

it comes with a limited range of features.
-kill #kills all connections but keeps server live
-kick #follow the promps to kill a specific connection
-con  #lists connected clients
'''

class Server:

    def __init__(self,port=5000):
        self.HOST_IP = ''#str(socket.INADDR_ANY)
        self.HOST_PORT = port
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
        self.connections = []
        self.threads = []
        self.queue = queue.Queue()

    '''
    close_connection()
    helper meathod to close a single function and remove it from
    the connections list. This function assumes the client has 
    already issued the close command.
    '''
    def close_connection(self,conn,addr):
        conn.close()
        self.connections.remove((conn,addr))

    '''
    kill_connections()

    broadcasts the kill command so clients close all
    client side connections. then loops through 
    connections and closes each connection.
    finally, resets connections
    '''
    def kill_clients(self):
        print('running kill clients')
        #send kill command to all clients
        '''
        broadcast kill command
        '''
        self.broadcast_message('kill')

        '''
        close connections
        '''
        for conn, addr in self.connections:
            print('closing connection with {}'.format(addr))
            conn.close()
            print('closed connection {}'.format(addr))
        
        '''
        clear server connections memory
        '''
        self.connections =[] 

        
    def show_conns(self):
        for i in range (0,len(self.connections)):
            print('Connection: {} \tIndex:{}'.format(self.connections[i][1],i))

    '''
    def server_input_thread()
    this daemon gets server input and is used for running commands.
    currently there are two commands. 
    
    "kill" will close all client
    connections from client side and server side.

    "con" will show all active connections
    '''
    def server_input_thread(self):
        while True:

            data = input('')

            '''
            kill clients
            '''
            if data == 'kill':
                self.kill_clients()
            
            if data == 'kick':
                self.show_conns()
                index = input('Enter index: ')
                #try:
                index = int(index)
                conn  = self.connections[index][0]
                addr  = self.connections[index][1]
                self.send_message('kill',conn,addr)
                self.close_connection(conn,addr)
                self.pickle_connections()
                self.show_conns()
                #except:
                #    print('not a valid input')

            '''
            loop throuh connections and print all
            '''
            if data == 'con':
                self.show_conns()


    def create_socket(self):
        #to bind the socket object to an ipv4 port we need to pass a host, port tuple
        #use with to ensure connection is closed
        print('connecting to socket')
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('socket connected')
        except socket.error:
            print ('Failed to open socket')
            sys.exit()

        #Bind socket to port
        print('binding socket to port')
        try:
            self.socket.bind(self.IPV4_ADDRESS)
            print('socket bound to port {}'.format(self.HOST_PORT))
            return True
        except socket.error :
            print('failed to bind socket\nexiting...')
            sys.exit()

        #starts a new thread to echo text. this is to test if multiple servers will run together

        #recieve data
    '''
    secho_server()
    lets the client communicate with the server and other clients
    the daemon thread runs in the background and has the following 
    features.

    push data to the queue for the broad_cast_message thread.

    close the server side connection to the socket if the (q) 
    command is issued. The client side will close first.
    '''
    def echo_server(self,conn,addr,queue):
        print('connection established with {}'.format(addr))
        while True:
            try:
                data, client = conn.recvfrom(self.BUFFSIZE)
                if data:
                    data = data.decode('UTF-8')

                    '''
                    if quit command is issued the client has closed its side of the connection
                    to complete closing teh socket the connection needs to be closed and removed
                    from the connections.
                    '''
                    if data == '(q)':
                        print('{} has disconnected'.format(addr))
                        self.close_connection(conn,addr)
                        self.pickle_connections()
                        return

                    '''
                    prints the data and puts it on the queue
                    '''
                    print ("data: {}".format(data))
                    queue.put((data,addr))
            except socket.error as e:
                print('echo_error')
                print(e)
                '''
                exit thread
                '''
                sys.exit()


    '''
    boradcast_message_thread
    This daemon thread is used to broadcast messages to
    all clients in the connections list.

    It will not send the message to it's own connection.
    '''
    def broadcast_message_thread(self,queue):
        while True:
            '''
            try recieving data pushed to the queue.
            '''
            try: 
                data,origin_addr = queue.get()
            except ValueError as e:
                print (e)

            '''
            loop through connections. if the connection is the origin
            skip it. otherwise sendall() socket data with o
            '''
            for conn, addr in self.connections:
                if origin_addr == addr:
                    continue
                try:
                    if data:
                        conn.sendall(bytes('{}>{}'.format(origin_addr,data),'UTF-8'))
                except ValueError as e:
                    print (e)
    '''
    signal_handler()
    elegantly handle ctrl+c exiting by closing all connected 
    sockets.
    '''

    def signal_handler(self,signal, frame):
        self.kill_clients()
        print()

        '''
        wait a short delay before closing the system
        '''
        for i in range (3,0,-1):
            print('closing in: {}'.format(i))
            time.sleep(1)
        sys.exit()

    '''
    pickle_connections
    I was originally going to try use an exploit in pickle that lets me execute code with
    the first argument so I could run python code on clients by sending it as a pickle file.
    Alas it appeared that I would have to change my code too much to make it work. I thought it
    would be a fun example of social engineering.

    Anyway this function pickles the connection tuple so that it can be sent over sockets easily
    it pickles the data and sends the bytes to the client
    '''
    def pickle_connections(self):
            pickled_conns = [addr[1] for addr in self.connections]
            pickled_conns=pickle.dumps(pickled_conns)
            self.broadcast_bytes(pickled_conns)   


    '''
    boradcast_bytes
    this function sends byte data to connect clients
    '''
    def broadcast_bytes(self,data):
        for conn, addr in self.connections:
            try:
                print(addr)         
                conn.sendall(data)
            except ValueError:
                print('connection with {} ended abruptly'.format(addr))
                self.close_connection(conn,addr)
            # return
    '''
    broadcast_message
    this function broadcasts strings to all connected clients
    '''
    def broadcast_message(self,data,override=True):
        for conn, addr in self.connections:
            try:
                print(addr)         
                conn.sendall(bytes('{}'.format(data),'UTF-8'))
            except BrokenPipeError:
                print('connection with {} ended abruptly'.format(addr))
                self.close_connection(conn,addr)

            # return

    '''
    send_message

    sends a message to an individual connection
    '''
    def send_message(self,data,conn,addr):
        try:
            print(addr)         
            conn.sendall(bytes('{}'.format(data),'UTF-8'))
        except ValueError as e:
            print(e)
        # return

    '''
    launch
    this function runs the required functions to start the server. It starts various threads
    and enters the main loop where it listens for new connections
    '''
    def launch(self,attempts=10):

        print("listening for connections")
        self.socket.listen(attempts)
        
        #c.gui.send(c.gui.message + '\n')
        print("Starting broadcast thread")
        broadcast_thread = threading.Thread(target=self.broadcast_message_thread,args=(self.queue,))
        broadcast_thread.daemon = True
        broadcast_thread.start()
        
        print("Starting Server <command> listener")
        server_input = threading.Thread(target=self.server_input_thread)
        server_input.daemon = True
        server_input.start()

        #accept connection


        while True:
            conn,addr = self.socket.accept()
            #print('connection formed with addr: {} and conn: {} '.format(addr,conn))
            self.connections.append((conn,addr))
        
        
            pickled_conns = [addr[1] for addr in self.connections]
            pickled_conns=pickle.dumps(pickled_conns)
            self.broadcast_bytes(pickled_conns)    
            self.threads.append(threading.Thread(target=self.echo_server,args=(conn,addr,self.queue,)))
            self.threads[-1].start()
            self.broadcast_message('\n\n-----------------------------------\n{} Connected.\nGive them a warm welcome\n-----------------------------------\n'.format(addr),addr)



#use argparse

def main():    
    s = Server(int(sys.argv[1]))
    s.create_socket()
    signal.signal(signal.SIGINT, s.signal_handler)
    s.launch()


if __name__ == '__main__':
    main()


