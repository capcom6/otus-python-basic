"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine(object):
    volume: float
    pistons: int
