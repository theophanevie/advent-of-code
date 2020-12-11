import pytest
import os
from ..src.day11 import check_secondpart, check_firstpart

def test_day4_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 37 == check_firstpart(path)

def test_day4_simple():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 26 == check_secondpart(path)
    
