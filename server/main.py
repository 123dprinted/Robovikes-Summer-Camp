import time
import socket

import rich
import rich.progress

from joystick import Manager
from rich.progress import Progress
from pyjoystick.sdl2 import Key, Joystick, run_event_loop

class RobotController():
    def __init__(self, roboid, debug):
        self.roboid = roboid
        self.debug = debug
        self.HOSTS = ['192.168.50.246', '192.168.50.245']
        self.PORTS = ['5555', '5556']

        self.manager = None

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

        if self.debug:
            rich.print("[bold yellow]Starting joystick handler in debug mode![/bold yellow]")
            
        self.manager = Manager(self.debug)

        while self.manager.running:
            self.manager.main()

            if self.send_data:
                pass

        self.manager.kill()

    def main(self):
        self.connect()
        self.handshake()
        self.handle()

if __name__ == "__main__":
    try:
        controller = RobotController(0, True)
        controller.main()
        rich.print("[bold red]Shutting down...[/bold red]")
    except KeyboardInterrupt:
        rich.print("[bold red]Shutting down...[/bold red]")
    except TimeoutError:
        rich.print("[bold red]Timeout. Is your robot on? Are you connecting to the right robot?[/bold red]")