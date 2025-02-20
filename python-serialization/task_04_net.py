#!/usr/bin/python3
# task_04_net.py
"""Modules for tcp json socket"""

import socket
import json


def start_server():
    """server socket"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 1234))
    server_socket.listen(1)
    client_socket, client_ip = server_socket.accept()
    data_recieved = client_socket.recv(1024).decode()
    recieved_dict = json.loads(data_recieved)
    print("Received dictionary:", recieved_dict)
    client_socket.close()
    server_socket.close()


def send_data(dictionnay):
    """client socket"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 1234))
    data_to_send = json.dumps(dictionnay)
    client_socket.send(data_to_send.encode())
    client_socket.close
