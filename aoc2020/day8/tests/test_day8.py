import pytest
import os
from ..src.day8 import check, check_firstpart

def test_day4_firstpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test.txt')
    assert 5 == check_firstpart(path)

def test_day4_secondpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test.txt')
    assert 8 == check(path)
