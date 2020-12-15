import pytest
import os
from ..src.day14 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 165 == check_firstpart(path)

def test_input():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input.txt')
    assert 13727901897109 == check_firstpart(path)

def test_basic2():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-part2.txt')
    assert 208 == check_secondpart(path)
    
