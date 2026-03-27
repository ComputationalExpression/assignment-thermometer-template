import time
import random
from typing import Any

class Pin:

    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, id: Any, mode: Any, *args, **kwargs):
        self.id = id
        self.mode = mode
        self.val = 0
        self.reads = 0

    def value(self, reads: int = 3) -> int:
        if reads == 0:
            return random.randint(0 ,1)
        if self.reads == reads:
            return 0
        self.reads += 1
        return 1

    def on(self):
        self.val = 0
        print(self.id, self.val)

    def off(self):
        self.val = 1
        print(self.id, self.val)

class ADC:
    
    def __init__(self, sample_ns, *kwargs):
        self.id = sample_ns
        self.u16 = random.randint(1, 65535)
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])
    
    def read_u16(self, **kwargs) -> int:
        try:
            self.u16 = kwargs["value"]
        except KeyError:
            self.u16 = random.randint(1, 65535)
        if self.id == 4:
            return self.u16
        return 0
    
    def read_uv(self, *args) -> float:
        return (self.u16 * (3.3/ 65535)) / 1000