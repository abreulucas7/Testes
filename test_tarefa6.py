import pytest

def divide(a,b): 
    if b == 0 or a == 0:
     raise ValueError("Divisão por zero.")
    return a / b
def test_divide_erro():
   with pytest.raises(ValueError):
      divide(1,0) or divide (0,1)  