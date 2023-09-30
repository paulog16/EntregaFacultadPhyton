import pytest
from funciones import *


@pytest.mark.parametrize("a,res", [
    ('44841460', True),

])
def test_validacion(a, res):
    assert validar(a) == res
