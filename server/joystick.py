import pygame
import rich

from joystick_handler import JoystickHandler

class Manager:
    def __init__(self, debug):
        pygame.init()

        self.debug = debug

        info = pygame.display.Info()
        self.screen = pygame.display.set_mode((info.current_w, int(info.current_h/3)))
        self.clock = pygame.time.Clock()
        self.running = True

        self.joystick_handler = JoystickHandler()


    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.JOYDEVICEADDED:
                self.joystick = pygame.joystick.Joystick(event.device_index)
                self.joystick_handler.add_joystick(self.joystick)
                rich.print("[bold green]Joystick added![/bold green]")
            if event.type == pygame.JOYBUTTONDOWN and self.debug:
                rich.print("[bold yellow]Button pressed.[/bold yellow]")

    def draw(self):
        self.screen.fill("black")

        try:
            self.joystick1 = self.joystick_handler.get_joystick(0)
        except:
            pass

        self.clock.tick(60)
        pygame.display.update()

    def kill(self):
        pygame.quit()


    '''
    GAME LOOP
    '''
    def main(self):
        self.events()
        self.draw()
