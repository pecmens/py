import math


class Mathtool:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addtool(self):
        return self.x + self.y

    def subtool(self):
        return self.x - self.y

    def multool(self):
        return self.x * self.y

    def divtool(self):
        return self.x / self.y

    def powtool(self):
        return self.x ** self.y

    def modtool(self):
        return self.x % self.y

    def exttool(self):
        return self.x ** (1 / self.y)

    def logtool(self):
        return math.log(self.x, self.y)
