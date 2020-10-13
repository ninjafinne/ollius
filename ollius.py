#!/usr/bin/env python3

class Length:
  def __init__(self, m):
    self._m = m
  def m(self):
    return self._m
  def cm(self):
    return self._m * 100

class Area:
  def __init__(self, m2):
    self._m2 = m2
  def m2(self):
    return self._m2
  def cm2(self):
    return self._m2 * 10000

class Square:
  '''
  x is expected as type Length
  '''
  def __init__(self, x):
    self.x = x
  def area(self):
    return Area(self.x.m() * self.x.m())

if __name__ == '__main__':
  s = Square(Length(2.0))
  print(f'Our square area is {s.area().cm2()} cm^2')
