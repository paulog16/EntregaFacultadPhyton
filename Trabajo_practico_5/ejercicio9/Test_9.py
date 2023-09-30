import pytest
from funciones9 import *

@pytest.mark.parametrize('a,b,res',[
    ('usuario1','asdasd',True)
])

def test_9(a,b,res):
    assert login(a,b)==res