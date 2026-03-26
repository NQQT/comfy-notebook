import argparse
import os
import socket
import subprocess
import sys
import time
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process

import psutil


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


def make_cors_proxy(target_port, proxy_port):
    class CORSProxy(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # suppress default logging

        def do_OPTIONS(self):
            self.send_response(200)
            self._send_cors_headers()
            self.end_headers()

        def _send_cors_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')

        def _proxy(self):
            url = f'http://localhost:{target_port}{self.path}'
            body = None
            if self.command in ('POST', 'PUT', 'PATCH'):
                length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(length) if length else None

            req_headers = {k: v for k, v in self.headers.items()
                           if k.lower() not in ('host', 'content-length')}
            req = urllib.request.Request(url, data=body, headers=req_headers, method=self.command)
            try:
                with urllib.request.urlopen(req) as resp:
                    self.send_response(resp.status)
                    for k, v in resp.headers.items():
                        if k.lower() not in ('transfer-encoding',):
                            self.send_header(k, v)
                    self._send_cors_headers()
                    self.end_headers()
                    self.wfile.write(resp.read())
            except urllib.error.HTTPError as e:
                self.send_response(e.code)
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(e.read())

        do_GET = do_POST = do_PUT = do_DELETE = do_PATCH = _proxy

    return HTTPServer(('localhost', proxy_port), CORSProxy)


def run_cors_proxy(target_port, proxy_port):
    server = make_cors_proxy(target_port, proxy_port)
    print(f"CORS proxy running on port {proxy_port} → forwarding to {target_port}")
    server.serve_forever()


def run_app(env, command, port):
    print(command)
    subprocess.run(
        f'{command} & ssh -o StrictHostKeyChecking=no -p 80 -R0:localhost:{port} a.pinggy.io > log.txt',
        shell=True, env=env
    )


def print_url():
    print("waiting for output")
    time.sleep(2)
    sys.stdout.flush()

    found = False
    with open('log.txt', 'r') as file:
        end_word = '.pinggy.link'
        for line in file:
            start_index = line.find("http:")
            if start_index != -1:
                end_index = line.find(end_word, start_index)
                if end_index != -1:
                    print("😁 😁 😁")
                    print("URL: " + line[start_index:end_index + len(end_word)])
                    print("😁 😁 😁")
                    found = True
    if not found:
        print_url()
    else:
        with open('log.txt', 'r') as file:
            for line in file:
                print(line)


def find_and_terminate_process(port):
    for process in psutil.process_iter(['pid', 'name']):
        try:
            connections = process.connections()
            for conn in connections:
                if conn.laddr.port == port:
                    print(f"Port {port} is in use by process {process.info['name']} (PID {process.info['pid']})")
                    try:
                        process.terminate()
                        print(f"Terminated process with PID {process.info['pid']}")
                        return
                    except psutil.NoSuchProcess:
                        print(f"Process with PID {process.info['pid']} not found")
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue


def main():
    parser = argparse.ArgumentParser(description='Start pinggy with shell command and port')
    parser.add_argument('--command', help='Specify the command to run with pinggy')
    parser.add_argument('--port', help='Specify the port')
    args = parser.parse_args()

    print(args.port)
    print(args.command)
    env = os.environ.copy()
    target_port = int(args.port)
    proxy_port = target_port + 1  # CORS proxy sits one port up
    command = args.command

    if is_port_in_use(target_port):
        find_and_terminate_process(target_port)
    else:
        print(f"Port {target_port} is free.")

    if is_port_in_use(proxy_port):
        find_and_terminate_process(proxy_port)

    open('log.txt', 'w').close()

    # Run app on target_port, proxy on proxy_port, pinggy tunnels proxy_port
    p_app = Process(target=run_app, args=(env, command, proxy_port,))
    p_proxy = Process(target=run_cors_proxy, args=(target_port, proxy_port,))
    p_url = Process(target=print_url)

    p_proxy.start()
    time.sleep(0.5)  # let proxy start before tunneling
    p_app.start()
    p_url.start()
    p_app.join()
    p_url.join()


if __name__ == '__main__':
    main()
