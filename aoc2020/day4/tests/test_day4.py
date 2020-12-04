import pytest
import os
from ..src.day4 import checkpassportvalidity

def test_day4():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input')
    for filename in os.listdir(path):
        filename = filename.split('-')
        if filename[0] == 'test':
            assert int(filename[1]) == checkpassportvalidity(\
                os.path.join(path, '-'.join(filename)))
