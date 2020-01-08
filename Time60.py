import numpy as gs

class Time60(object):
    def __init__(self, hr, mint):
        self.hr = hr + int(mint/60)
        self.mint = gs.mod(mint, 60)
    
    def __str__(self):
        return '{}:{:02d}'.format(self.hr, self.mint)

    __repr__ = __str__

    def __add__(self,other):
        return self.__class__(self.hr+ other.hr, self.mint+other.mint)

    def __iadd__(self, other):
        self.hr += other.hr +int((self.mint+other.mint)/60)
        self.mint += other.mint - int((self.mint+other.mint)/60)*60
        return self