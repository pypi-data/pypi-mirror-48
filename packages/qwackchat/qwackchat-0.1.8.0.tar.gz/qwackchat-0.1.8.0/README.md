#Thank you for installing the QwackChat chatroom.

**Qwackchat** is a private lan based chatroom written in python3. The chatroom allows users to communicate with one another locally via sockets and reduces the ability for **data harvesters** such as google, amazon, facebook and others from viewing your communications.

**Qwackchat** communications do not use any form of encryption and will be visible to network administrators and experienced computer users.

**Qwackchat** communications will likely also be visible to your **ISP** if you use their provided router however you may improve security by using a *secure third party router*.

**Qwackchat** may also work over your public IP with port forwarding however this is not tested and will likely further reduce its security and *may induce addition vunerabilites*.

**The Author of QwackChat claims no liability or responsibility for any actions take by *you* the user.**


##Installation

1. open a python3 terminal 
2. type pip3 install qwackchat

##Dependencies

sqwackchat.py, qwackchat.py qui.py

##System Requirements

A linux or Mac computer with python3 & pip3 installed

##Hosting a server 

1. open a terminal
2. type *ifconfig* and find your lan address **typically 10.0.xx.xx or 192.168.xx.xx**
3. type *sqwackchat portnumber* **a good range is 5000-65000**
4. tell users your lan address and port number

**sub your lan address for public ip and forward your desired port to try over your public IP**


##Running a client

1. aquire server ip and port from host 
2. open a terminal
3. type *qwackchat server_ip port*

##Using the GUI

**This is  fairly straight forward**

run a client
write text in the input box **Bottom text box**
send messages with the send button **left of bottom field**
read sent messages in the output box **Top text field**
view connected clients in the connections box **right text box**
