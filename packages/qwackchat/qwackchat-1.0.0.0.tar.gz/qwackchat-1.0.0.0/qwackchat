#!/usr/bin/env python

import socket
import sys
import time
from datetime import datetime
import threading
import signal
import gui
import pickle
'''
The qwackchat class is used to setup a qwackchat client that will connect to
the server and communicate with other clients via the GUI interface
'''
class Client:

    def __init__(self,ip='10.0.74.88',port=5000):
        self.HOST_IP = ip #124.169.15.130'#'49.181.246.235'
        self.HOST_PORT = int(port)  #works on port 80 but not 5000 w definitly a firewall issue
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
        self.msg_buffer = ''
        self.local_port = ()
        self.exit = False
        self.gui = None
        self.messages=[]
        self.message = None
        self.rcv_message = None
        self.connections = []
        self.new_connection = False
    '''
    create_socket
    Creates a socket object to connect to host address
    '''
    def create_socket(self):
        print("Creating socket")
        print(self.IPV4_ADDRESS)
        
        #to bind the socket object to an ipv4 port we need to pass a host, port tuple
        

        #use with to ensure connection is closed
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('Socket Created')
        except socket.error as e:
            print (e)
    '''
    connect_to_server
    attempts to connect to the host server. must be called after the socket object is created.
    will exit on failure
    '''

    def connect_to_server(self):
        print('Connecting to QwackChat')
        
        try:
            self.socket.connect(self.IPV4_ADDRESS)
            self.local_port = self.socket.getsockname()
            print('Host address-->     {}:{}'.format(c.HOST_IP,c.HOST_PORT))
            print('Local address-->    {}:{}'.format(self.local_port[0],self.local_port[1]))
            print("Connected @ {}".format(str(datetime.now())))
        except:
            print ('Connection to-->    {}:{} failed\nExiting'.format(self.HOST_IP,self.HOST_PORT))
            sys.exit()

    '''
    send_message
    sends a message to the server 
    '''
    def send_message(self, message):
        msg = bytes(message,'UTF-8')
        try:
            self.socket.send(msg)
        except socket.error as e:
            print(e)
    '''
    returns data transimtted from the server
    '''

    def recieve_message(self):
        data = self.socket.recv(self.BUFFSIZE)
        if len(data) > 0:
            return data
        return None
    '''
    signal_handler
    is used to handle quitting elegantly. sends a "(q)" to the server so
    the server knows it has been disconnected (although this may no longer be necessary)
    then exits 
    '''
    def signal_handler(self,signal, frame):
        try:
            self.send_message('(q)')
            self.socket.close()
            sys.exit()
        finally:
            print('\nquitting')
            sys.exit()

    '''
    get_message_thread
    this thread is a loop that recieves messages from the socket connection.
    on a message recieved it checks if it's a pickle (possibly badly if im a noob
    and I actually did build the exploit in) if the message is kill the server has
    closed the connection and the socket will close. otherwise it deletes the message
    '''        
    def get_message_thread(self):
        while True:
            recieved_msg = c.recieve_message()#.decode('utf-8')
            try:
                clients = pickle.loads(recieved_msg)
                self.new_connection = True
                self.connections = clients
                
                print(clients)
            except:
                if not recieved_msg:
                    self.exit =True
                    sys.exit()
                self.rcv_message = recieved_msg.decode('utf-8')
                if self.rcv_message == 'kill':
                    print('connection closed by server')
                    self.exit = True
                    return
                print(self.rcv_message)   

    '''
    i refuse to comment this function with helpful information
    '''
    '''def send_message_thread(self):
        while True:
            self.message = input('')
    '''
'''
setup the socket and gui
'''


c = Client(sys.argv[1],sys.argv[2])

c.create_socket()
c.connect_to_server()
c.gui = gui.Qui()
c.gui.recieve('\nHi and welcome to Qwackchat\nYour connection > [{}:{}]\n'.format(c.local_port[0],c.local_port[1]))

'''
start send and recieve threads
'''

recv_thread = threading.Thread(target=c.get_message_thread)
recv_thread.daemon = True
recv_thread.start()

'''
send_thread = threading.Thread(target=c.send_message_thread)
send_thread.daemon = True
send_thread.start()
'''



signal.signal(signal.SIGINT, c.signal_handler)

'''
this is the main loop which handles all gui operations as the tkinter module is not threadsafe

'''
while not c.exit:
    
    if c.gui.exit:
        print('close')
        c.send_message('(q)')
        c.exit=True
        break

    '''
    if the gui has a message
    '''
    if c.gui.message:
        c.send_message(c.gui.message)
        c.gui.message = None

    if c.rcv_message:
        c.gui.recieve(c.rcv_message)
        c.rcv_message = None
        c.gui.message = None

    if c.new_connection:
        c.gui.update_connections(c.connections)
        c.new_connection = False

    if c.message:
        if c.message == '(q)':
            c.send_message('(q)')
            c.exit=True
        try:
            c.send_message(c.gui.send(c.message ))
        except:
            pass
        c.message = None
    try:
        c.gui.window.update_idletasks()
        c.gui.window.update()
    except:
        c.send_message('(q)')
        sys.exit()
sys.exit()


