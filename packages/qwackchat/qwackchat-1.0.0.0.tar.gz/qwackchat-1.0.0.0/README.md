# Thank you for installing the QwackChat chatroom.

**Qwackchat** is a private lan based chatroom written in python3. The chatroom allows users to communicate with one another locally via sockets and reduces the ability for **data harvesters** such as google, amazon, facebook and others from viewing your communications.

**Qwackchat** communications do not use any form of encryption and will be visible to network administrators and experienced computer users.

**Qwackchat** communications will likely also be visible to your **ISP** if you use their provided router however you may improve security by using a *secure third party router*.

**Qwackchat** may also work over your public IP with port forwarding however this is not tested and will likely further reduce its security and *may induce addition vunerabilites*.

**The Author of QwackChat claims no liability or responsibility for any actions take by *you* the user.**

**NOTE: the terminal application does not use the CLI for communication anymore. prior versions allowed this but the feature has since been discontinuted**

## System requirements
1. A linux computer
2. the [tkinter](https://www.activestate.com/products/activetcl/downloads/) package must be downloaded manually prior to running.
3. python3 installed
## Installation

1. open a python3 terminal 
2. type pip3 install qwackchat

## Dependencies

sqwackchat.py, qwackchat.py qui.py

## Hosting a server 

1. open a terminal
2. type *ifconfig* and find your lan address **typically 10.0.xx.xx or 192.168.xx.xx**
3. type *sqwackchat portnumber* **a good range is 5000-65000**
4. tell users your lan address and port number

**sub your lan address for public ip and forward your desired port to try over your public IP**


## Running a client

1. aquire server ip and port from host 
2. open a terminal
3. type *qwackchat server_ip port*

## Using the GUI

**This is  fairly straight forward**

run a client
write text in the input box **Bottom text box**
send messages with the send button **left of bottom field**
read sent messages in the output box **Top text field**
view connected clients in the connections box **right text box**



# User Interaction and Experience

It's an anonamous chatroom with a user interface that lets users talk to
one another. As people are well familiar with chat applications today 
this is a very straight forward app to use.

the user will be able to see other users in the chat in the right hand panel
and send messages by typing into the the input box at the bottom and clicking
send.

upon data being sent by the user or recieved from another user it will appear
in the chat window at the top.

the server side is even more straight forward. The server is started with a single
command and then is left to idle for the duration of communication. there are a few
commands packaged into the server to control users that are connected.

Standard and simple. That's our motto~!

#### Clients:

![alt text](https://i.imgur.com/UnGSVOQ.png "server image")

#### Server:

![alt text](https://i.imgur.com/2Jtcx77.png "client image")



