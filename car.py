
class Car:

    def __init__(self, speed = 0):
        self.speed = speed
        self.color = "white"

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def accelerate(self):
        return "faster"

    def brake(self):
        return "brake"

    def set_color(self, color):
        if color == "":
            return
        self.color = color