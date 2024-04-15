import random

class Circle:
    def __init__(self, x, y, diameter, speed, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.speed = speed
        self.color = color

    def move(self):
        self.y += self.speed

    def reset(self, width, height):
        if self.y > height:
            self.y = random.uniform(-500, -50)
            self.x = random.uniform(0, width)
