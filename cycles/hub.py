from .cyclometer import log
from .wheel import Wheel

class Hub:
    def __init__(self, name='anon'):
        self.name = name
        self.wheel = Wheel(10)
        log.info(f'Hub \'{name}\' Initialized')
