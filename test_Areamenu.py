import Areamenu
import pytest
def test_area_of_rec():
    l=4
    b=5
    res=Areamenu.area_of_rec(l,b)
    assert res==l*b
def test_perimeter_of_rec():
    l=4
    b=5
    res=Areamenu.perimeter_of_rec(l,b)
    assert res==2*(l+b)
def test_area_of_circle():
    r=5
    res=Areamenu.area_of_circle(r)
    assert res==22/7*(r**2)
def test_area_of_square():
    x=5
    res=Areamenu.area_of_square(x)
    assert res==x**2
def test_area_of_tri():
    b=5
    h=7
    res=Areamenu.area_of_tri(b,h)
    assert res==1/2*(b*h)