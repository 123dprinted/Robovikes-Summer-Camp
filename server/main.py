import time
import socket

import rich
import rich.progress

from rich.progress import Progress

class RobotPanel():
    def __init__(self, roboid):
        self.roboid = roboid
        self.HOSTS = ['192.168.50.246', '192.168.50.245']
        self.PORTS = ['5555', '5556']

        self.robot_socket = None
        self.send_data = False

    def connect(self):
        self.robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.robot_socket.connect((self.HOSTS[self.roboid], int(self.PORTS[self.roboid])))
    
    def handshake(self):
        while True:
            data = self.robot_socket.recv(1024)

            if data.decode('utf-8') == '-2':
                rich.print(f"[bold green]Connection successful. Hello from robot[/bold green] {self.roboid}!") 
                break
    
    def handle(self):
        rich.print(f"[bold green]Connected to ID:[/bold green] {self.roboid}")

        while True:
            if self.send_data:
                pass

    def main(self):
        self.connect()
        self.handshake()
        self.handle()

if __name__ == "__main__":
    try:
        panel = RobotPanel(1)
        panel.main()
    except KeyboardInterrupt:
        rich.print("[bold red]Shutting down...[/bold red]")