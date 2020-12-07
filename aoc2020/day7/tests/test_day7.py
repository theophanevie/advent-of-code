import pytest
import os
from ..src.day7 import check, check_firstpart

def test_day4_firstpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test.txt')
    assert 4 == check_firstpart(path)

def test_day4_secondpart():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join('..', 'input', 'provided-test-part2.txt')
    assert 126 == check(path)
