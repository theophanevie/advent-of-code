import pytest
import os
from ..src.day22 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 306 == check_firstpart(path)
    assert 291 == check_secondpart(path)
    
