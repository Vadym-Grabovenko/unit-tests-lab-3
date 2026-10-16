import pytest

from delivery import delivery_cost

def test_delivery_happy_path_same_city():

    assert delivery_cost(1.0, True) == 32.0

def test_delivery_other_city_with_extra_weight():
    
    assert delivery_cost(2.5, False) == 55.0

def test_delivery_boundary_exact_one_kg():
   
    assert delivery_cost(1.0, False) == 40.0

def test_delivery_error_zero_weight():

    with pytest.raises(ValueError):
        delivery_cost(0, True)

def test_delivery_error_negative_weight():

    with pytest.raises(ValueError):
        delivery_cost(-2.5, False)