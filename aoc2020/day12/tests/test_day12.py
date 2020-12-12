import pytest
import os
from ..src.day12 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 286 == check_secondpart(path)
    assert 25 == check_firstpart(path)

def test_input():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input.txt')
    assert 52069 == check_secondpart(path)
    assert 582 == check_firstpart(path)
    
