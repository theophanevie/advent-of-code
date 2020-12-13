import pytest
import os
from ..src.day13 import check_secondpart, check_firstpart

def test_basic():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-simple.txt')
    assert 1068781 == check_secondpart(path)
    assert 295 == check_firstpart(path)

def test_input():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input.txt')
    assert 530015546283687 == check_secondpart(path)
    assert 207 == check_firstpart(path)
    
