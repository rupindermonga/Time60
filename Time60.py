import numpy as gs

class Time60(object):
    def __init__(self, hr, mint):
        self.hr = int(hr +round(mint/60,0))
        self.mint = gs.mod(mint, 60)
    
    def __str__(self):
        return '{}:{}'.format(self.hr, self.mint)