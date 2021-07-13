import string
import random

class Robot:
    def __init__(self):
        self.name = self.boot_robot()
    
    def boot_robot(self):
        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        numbers = "".join(random.choices(string.digits, k=3))
        self.name = letters + numbers
        return self.name
    
    def reset(self):
        robot = Robot()
        robot.name = self.boot_robot()
