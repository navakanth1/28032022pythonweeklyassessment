import Prism
from math import sqrt
import pytest
def test_surface_area():
    l=3
    w=5
    h=6
    res=Prism.surface_area(l,w,h)
    assert res==2*(w*l+h*l+h*w)
def test_volume():
    l=5
    w=7
    h=4
    res=Prism.volume(l,w,h)
    assert res==w*h*l
def test_space_diagonal():
    l=2
    w=6
    h=8
    res=Prism.space_diagonal(l,w,h)
    assert res==sqrt(w**2+h**2+l**2)
