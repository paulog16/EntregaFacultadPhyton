import pytest
from funciones4 import *

@pytest.mark.parametrize('a,b,res',[
    (4,2,True),
    (5,3,False),
])
def test_multi(a,b,res):
    assert multiplo(a,b)==res