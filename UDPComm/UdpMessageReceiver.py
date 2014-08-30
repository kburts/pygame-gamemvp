__author__ = 'Jeff'

import socket
import threading
import time


class UdpMessageReceiver(threading.Thread):
    def __init__(self, udp_ip='127.0.0.1', udp_port=5005):
        threading.Thread.__init__(self)
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.udp_ip, self.udp_port))
        self.keep_alive = True
        self.data = None

    def run(self):
        while self.keep_alive:
            self.data = self.sock.recv(1024) # buffer size is 1024 bytes

    def get_data(self):
        return self.data

    def kill_receiver(self):
        self.keep_alive = False

if __name__ == '__main__':
    msgReceiver = UdpMessageReceiver()
    msgReceiver.start()
    for i in xrange(0,20):
        time.sleep(0.5)
        print msgReceiver.get_data()