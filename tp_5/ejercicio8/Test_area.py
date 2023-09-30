import pytest 
from funciones8 import *

@pytest.mark.parametrize('a,res',[
    (4,25.12),
])

def test_area(a,res):
    assert area(a)==res