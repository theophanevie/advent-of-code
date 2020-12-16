import pytest
import os
from ..src.day16 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input.txt')
    assert 26941 == check_firstpart(path)
    assert 634796407951 == check_secondpart(path)
    
