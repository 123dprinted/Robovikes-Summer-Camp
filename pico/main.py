from machine import PWM, Pin
from picozero import LED, pico_led

import network
import socket
import utime

class Robot():
    def __init__(self):
        self.HEADERSIZE = 10
        self.PASSWORD = 'canham1020'
        self.SSID = 'stalag13_24ghz'
        self.PORT = 5555 #change based on robot
        
        self.server_running = True
        self.server_socket = None
        self.wlan = None
        
    def connect(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.SSID, self.PASSWORD)
        
        while self.wlan.isconnected() == False:
            print('Waiting for connection...')
            utime.sleep(1)
            
        ip = self.wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        
        return ip
        
    def start_server(self):
        ip = self.connect()
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, self.PORT))
        self.server_socket.listen(5)
        
        print("Server started. Listening for connections...")
        
        while self.server_running:
            client_socket, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_socket.send(str(-2).encode())
            print("Sent confirmation")
            pico_led.on()
        
        self.server_socket.close()
        
    def blink(self, times, interval):
        for x in range(times):
            pico_led.on()
            utime.sleep(interval)
            pico_led.off()
            utime.sleep(interval)
            
        
if __name__ == "__main__":
    try:
        robot = Robot()
        robot.start_server()
    except KeyboardInterrupt:
        robot.wlan.disconnect()
        pico_led.off()
    except OSError as e:
        print(e)
        robot.wlan.disconnect()
        pico_led.off()
        robot.blink(3, 0.5)        
        
        
        