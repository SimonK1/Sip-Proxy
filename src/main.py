import sipfullproxy
import re
import string
import socket
# import threading
import sys
import time
import logging
import socketserver as SocketServer


def startServer():
    host = '0.0.0.0'
    port = 5060

    # Changing IP recognition according to Linux systems
    hostname = socket.gethostname()

    if len(sys.argv) > 0:
        ipaddress = sys.argv[0]
    else:
        my_ip = socket.gethostbyname_ex(hostname)[-1]
        ipaddress = my_ip[1]

    # Logs
    logging.basicConfig(format='(%(asctime)s) > %(message)s', filename='proxy.txt', level=logging.INFO,
                        datefmt='%a, %d %b %Y %H:%M:%S')
    logging.info('Proxy server spusten￿ý na Host: %s, Port: %d', host, port)

    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, port)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, port)
    server = SocketServer.UDPServer((host,port), sipfullproxy.UDPHandler)
    print("Server is running...")

    server.serve_forever()

