import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
b = board.get_pin('d:2:o')      #b
a = board.get_pin('d:3:o')      #a
f = board.get_pin('d:4:o')      #f
g = board.get_pin('d:5:o')      #g
dp = board.get_pin('d:6:o')     #dp
c = board.get_pin('d:7:o')      #c
d = board.get_pin('d:8:o')      #d
e = board.get_pin('d:9:o')      #e

it = pyfirmata.util.Iterator(board)
it.start()

class Number:

    def __init__(self):
        a.write(0)
        b.write(0)
        c.write(0)
        d.write(1)
        e.write(0)
        f.write(0)
        g.write(0)
        dp.write(0)

    def zero(self):
        a.write(1)
        b.write(1)
        c.write(1)
        d.write(1)
        e.write(1)
        f.write(1)
        g.write(0)
        dp.write(0)

    def one(self):
        a.write(0)
        b.write(1)
        c.write(1)
        d.write(0)
        e.write(0)
        f.write(0)
        g.write(0)
        dp.write(0)
        
    def two(self):
        a.write(1)
        b.write(1)
        c.write(0)
        d.write(1)
        e.write(1)
        f.write(0)
        g.write(1)
        dp.write(0)

    def three(self):
        a.write(1)
        b.write(1)
        c.write(1)
        d.write(1)
        e.write(0)
        f.write(0)
        g.write(1)
        dp.write(0)

    def four(self):
        a.write(0)
        b.write(1)
        c.write(1)
        d.write(0)
        e.write(0)
        f.write(1)
        g.write(1)
        dp.write(0)

    def five(self):
        a.write(1)
        b.write(0)
        c.write(1)
        d.write(1)
        e.write(0)
        f.write(1)
        g.write(1)
        dp.write(0)

    def six(self):
        a.write(1)
        b.write(0)
        c.write(1)
        d.write(1)
        e.write(1)
        f.write(1)
        g.write(1)
        dp.write(0)

    def seven(self):
        a.write(1)
        b.write(1)
        c.write(1)
        d.write(0)
        e.write(0)
        f.write(0)
        g.write(0)
        dp.write(0)

    def eight(self):
        a.write(1)
        b.write(1)
        c.write(1)
        d.write(1)
        e.write(1)
        f.write(1)
        g.write(1)
        dp.write(0)

    def nine(self):
        a.write(1)
        b.write(1)
        c.write(1)
        d.write(1)
        e.write(0)
        f.write(1)
        g.write(1)
        dp.write(0)

while True:
    Number().zero()
    time.sleep(1)
    Number().one()
    time.sleep(1)
    Number().two()
    time.sleep(1)
    Number().three()
    time.sleep(1)
    Number().four()
    time.sleep(1)
    Number().five()
    time.sleep(1)
    Number().six()
    time.sleep(1)
    Number().seven()
    time.sleep(1)
    Number().eight()
    time.sleep(1)
    Number().nine()
    time.sleep(1)

