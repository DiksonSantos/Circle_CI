import pytest
from principal import soma


def testa_soma():
    """testa"""
    assert soma(2, 4) == 6

def teste_subtrair():
    """Subtração"""
    assert subtrair(2, 2) == 0
