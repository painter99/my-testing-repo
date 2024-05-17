import pytest
import requests
import kalkulacka

def test_scitani():
    assert kalkulacka.add(x: 2, y: 3) == 5
    assert kalkulacka.add(x: 0, y: 1.5) == 1.5

def test_deleni():
    assert kalkulacka.divide(x: 2, y:0) == "Error Division by zero!"