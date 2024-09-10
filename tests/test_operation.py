from src.math_operation import add,sub
def test_add():
    assert add(2,3)==5
    assert add(5,3)==8

def test_sub():
    assert sub(4,3)==1
    assert sub(5,2)==3