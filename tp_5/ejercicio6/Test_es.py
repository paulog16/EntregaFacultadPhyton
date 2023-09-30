import pytest 
from funciones6 import *

@pytest.mark.parametrize('a,res',[
    ('hola','h o l a')
])
def test_es(a,res):
    assert espacio(a)==res