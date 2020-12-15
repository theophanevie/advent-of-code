import pytest
import os
from ..src.day15 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 436 == check_firstpart(path)
    
