import pytest
import os
from ..src.day10 import check_secondpart, check_firstpart

def test_day4_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 35 == check_firstpart(path)
    assert 8 == check_secondpart(path)

def test_day4_simple():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test.txt')
    assert 220 == check_firstpart(path)
    assert 19208 == check_secondpart(path)
    
