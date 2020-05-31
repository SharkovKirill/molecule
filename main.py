import turtle as t
import random as r
import math


class Mol():
    list = []
    colors = ['green', 'blue', 'purple', 'brown', 'yellow', 'orange', 'red']

    def __init__(self):
        self.radius = r.randint(25, 50)
        self.pos()
        self.color = Mol.colors[r.randint(0, len(Mol.colors) - 1)]
        Mol.list.append(self)

    def pos(self):
        self.x = r.randint(self.radius, 300 - self.radius)
        self.y = r.randint(self.radius, 300 - self.radius)
        for coords in Mol.list:
            if math.sqrt((((int(coords.x) - self.x) ** 2) + ((int(coords.y) - self.y) ** 2))) < int(
                    self.radius) + coords.radius:
                return self.pos()

    def show(self):
        t.penup()
        t.goto(self.x - self.radius, self.y)
        t.pendown()
        t.color(self.color)
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()

    def change(self):
        t.penup()
        t.goto(self.x - self.radius, self.y)
        t.pendown()
        t.color('white')
        t.fillcolor('white')
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()

        self.kof = r.uniform(1, 2)
        self.x = self.x + r.randint(-10, 10) * self.kof
        self.y = self.y + r.randint(-10, 10) * self.kof
        # while self.x>300-self.radius or self.x-self.radius<0 or self.y>300-self.radius or self.y-self.radius<0:
        #    self.x = self.x + r.randint(-10, 10) * self.kof
        #    self.y = self.y + r.randint(-10, 10) * self.kof
        for coords in Mol.list:
            if coords != self and (math.sqrt((((int(coords.x) - self.x) ** 2) + ((int(coords.y) - self.y) ** 2)))
                                   < int(self.radius) + coords.radius):
                return self.change()
        Mol.list.append(self)

    def all(self):
        self.show()
        self.change()
        self.show()

    def __str__(self):
        return str(self.x) + '  ' + str(self.y) + '  ' + str(self.radius)

    def __repr__(self):
        return self.__str__()


m1 = Mol()
m2 = Mol()
m3 = Mol()
m4 = Mol()

t.tracer(0)
while True:
    m1.all()
    m2.all()
    m3.all()
    m4.all()
    t.update()
