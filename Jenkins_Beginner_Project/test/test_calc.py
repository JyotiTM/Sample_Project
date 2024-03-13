import pytest
from Jenkins_Beginner_Project.src.calc import *


def test_add():
    assert add(5,4) == 9
	
def test_sub():
    assert sub(5,4) == 1
	
def test_mul():
    assert mul(5,4) == 20
	
def test_div():
    assert div(16,4) == 4