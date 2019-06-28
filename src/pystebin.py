#!/usr/bin/env python3

import http.server
import os
import random
import socket
import socketserver
import string
import threading

handler = http.server.SimpleHTTPRequestHandler

def generate_file_id(n):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k = n))

def save_data(data):
    file_name = generate_file_id(5)

    f = open(os.getcwd() + "/" + file_name, "w")
    f.write(data)
    f.close()

    return file_name

def start_server(port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    conn.bind(("0.0.0.0", port))
    conn.listen(10)
    print("[+] Server is up at port {}...".format(port))

    while True:
        current_client, addr = conn.accept()

        while True:
            data = current_client.recv(2048)
            if data:
                text = data.decode("utf-8")
                file_name = save_data(text).encode("utf-8")
                current_client.send(file_name)
                current_client.close()
                print("[+] File {} from {} saved!".format(file_name.decode("utf-8"), addr[0]))
                break

def start_http_server():
    if not os.path.exists("files"):
        print("[+] Creating folder to save files...")
        os.mkdir("files")

    file_directory = os.chdir("files")
    http = socketserver.TCPServer(("0.0.0.0", 80), handler)
    http.serve_forever()
    print("[+] HTTP server is up...")

if __name__ == "__main__":
    try:
        t = threading.Thread(target = start_http_server)
        t.setDaemon(True)
        t.start()
        start_server(9090)
    except KeyboardInterrupt:
        print("[+] Exiting...")
