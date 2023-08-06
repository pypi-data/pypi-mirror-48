#!/usr/bin/env python

import socket
import sys
import time
from datetime import datetime
import threading
import signal
import gui

class Client:

    def __init__(self,ip='10.1.1.6',port=5000):
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

    def send_message(self, message):
        msg = bytes(message,'UTF-8')
        try:
            self.socket.send(msg)
        except socket.error as e:
            print(e)
    
    def recieve_message(self):
        data = self.socket.recv(self.BUFFSIZE)
        return data
    
    def signal_handler(self,signal, frame):
        try:
            self.send_message('(q)')
            self.socket.close()
            sys.exit()
        finally:
            print('\nquitting')
            sys.exit()
            
    def get_message_thread(self):
        while True:
            print(self.HOST_PORT)
            recieved_msg = c.recieve_message().decode('utf-8')
            print(recieved_msg)
            self.rcv_message = recieved_msg
            if recieved_msg == 'kill':
                print('connection closed by server')
                self.exit = True
                return
            print(recieved_msg)   


    def send_message_thread(self):
        while True:
            self.message = input('')
    


c = Client(sys.argv[1],sys.argv[2])

    
c.create_socket()
c.connect_to_server()
c.gui = gui.Qui()
recv_thread = threading.Thread(target=c.get_message_thread,daemon=True)
recv_thread.start()


send_thread = threading.Thread(target=c.send_message_thread,daemon=True)
send_thread.start()



signal.signal(signal.SIGINT, c.signal_handler)

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
        print('gui')
     #   c.gui.send(c.gui.message + '\n')
        c.send_message(c.gui.message)
        c.gui.message = None

    if c.rcv_message:
        print('there is a message')
        c.gui.send(c.rcv_message )
        c.rcv_message = None
        c.gui.message = None


    if c.message:
        print('termi')
        if c.message == '(q)':
            c.send_message('(q)')
            c.exit=True
        c.send_message(c.gui.send(c.message ))
        c.message = None
    try:
        c.gui.window.update_idletasks()
        c.gui.window.update()
    except:
        print('ded')
        c.send_message('(q)')
        sys.exit()
sys.exit()

