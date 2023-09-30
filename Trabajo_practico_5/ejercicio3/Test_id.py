import pytest
from funciones3 import *
@pytest.mark.parametrize('a,b,res',[
    ('paulo guidolin','44841460','paulo4484')
])
def test_id(a,b,res):
    resultado=id_unico(a,b)
    assert resultado==res