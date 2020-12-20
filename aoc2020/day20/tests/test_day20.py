import pytest
import os
from ..src.day20 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 3 == check_firstpart(path)
    assert 3 == check_secondpart(path)
    
