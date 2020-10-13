#!/usr/bin/env python3

'''
v1
method based version
'''
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


'''
v2
Dictionary based version with more clean api
'''
LENGTH_TYPES = {
    'm': (lambda x: x),
    'cm': (lambda x: x * 100),
}
class Lengthv2:
    def __init__(self, m):
        self._m = m
    def get(self, unit):
        if unit not in LENGTH_TYPES:
            raise KeyError(f'unit {unit} not found')
        return LENGTH_TYPES[unit](self._m)
    
AREA_TYPES = {
    'm2': (lambda x: x),
    'cm2': (lambda x: x * 10000),
}
class Areav2:
    def __init__(self, m2):
        self._m2 = m2
    def get(self, unit):
        if unit not in AREA_TYPES:
            raise KeyError(f'unit {unit} not found')
        return AREA_TYPES[unit](self._m2)
        
class Squarev2:
  '''
  x is expected as type Lengthv2
  '''
  def __init__(self, x):
    self.x = x
  def area(self):
    return Areav2(self.x.get('m') * self.x.get('m'))
    
if __name__ == '__main__':
    '''v1'''
    s = Square(Length(2.0))
    print(f'Our square area is {s.area().cm2()} cm^2')
    
    '''v2'''
    s = Squarev2(Lengthv2(2.0))
    print(f'Our square area is {s.area().get("cm2")} cm^2')
