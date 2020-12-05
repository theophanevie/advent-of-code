import pytest
import os
from ..src.day5 import check, check_firstpart

def test_day5():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input')
    for filename in os.listdir(path):
        filename = filename.split('-')
        if filename[0] == 'test':
            assert int(filename[1]) == check_firstpart(\
                os.path.join(path, '-'.join(filename)))
