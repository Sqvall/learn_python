from abc import ABC, abstractmethod
from patterns_oop.command.simple_remote_control.gadgets import *


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    light: Light

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoorOpenCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()
