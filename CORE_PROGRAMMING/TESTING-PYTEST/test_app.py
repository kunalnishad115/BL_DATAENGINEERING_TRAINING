import pytest as p
from app import add,sub,divison

def test_greet():
  print("hello world")

@p.mark.smoke
def test_add():
  assert add(2,3)==5

@p.mark.smoke
def test_add1():
    assert add(1, 2) == 3

def test_add2():
    assert add(-1, 1) == 0

def test_add3():
    assert add(100, 200) == 300

@p.mark.smoke
def test_div():
   with p.raises(ZeroDivisionError):
      divison(23,0)

def test_sub():
  assert sub(5,5)==0



