import pytest
from funciones5 import *

@pytest.mark.parametrize('a,b,res',[
  (25,5,15),
  (10,15,12),  
])
def test_prom(a,b,res):
    assert prom(a,b)==res