# -*- coding: utf-8 -*-

from socketserver import BaseRequestHandler, UDPServer, ThreadingUDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print("connected to", self.client_address)
        msg, sock = self.request 
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    #serv = UDPServer(('localhost', 8086), TimeHandler)
    
    serv = ThreadingUDPServer(('localhost', 8086), TimeHandler) 
    serv.serve_forever()