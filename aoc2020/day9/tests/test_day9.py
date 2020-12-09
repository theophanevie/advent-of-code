import pytest
import os
from ..src.day9 import check_secondpart, check_firstpart

def test_day4_firstpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input-day9.txt')
    assert 15353384 == check_firstpart(path)

def test_day4_secondpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'input-day9.txt')
    assert 2466556 == check_secondpart(path)
