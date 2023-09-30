import pytest
from funciones7 import *
@pytest.mark.parametrize('a,res',[
  ([4,3,5,2,9,24],24),  
])
def test_minmax(a,res):
    assert maximo(a)==res
@pytest.mark.parametrize('a,res',[
  ([4,3,5,2,9,24],2),  
])
def test_minmax(a,res):
    assert minimo(a)==res
