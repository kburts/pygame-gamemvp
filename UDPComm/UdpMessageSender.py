__author__ = 'Jeff'

import socket


class UdpMessageSender():
    def __init__(self, udp_ip='127.0.0.1', udp_port=5005):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        self.sock.sendto(message, (self.udp_ip, self.udp_port))

if __name__ == '__main__':
    msg = UdpMessageSender()
    msg.send_message("test message")


