import pytest
from funciones2 import *

@pytest.mark.parametrize('a,res',[
    ('hola paulo','paulo')
])
def test_pf(a,res):
    assert pf(a)==res